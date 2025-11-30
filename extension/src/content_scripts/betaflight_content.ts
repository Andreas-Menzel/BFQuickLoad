/// <reference types="chrome" />

/**
 * content.ts
 * Version mit robusterer Event-Simulation, Bereitschaftsprüfung und Verbindungsmanagement.
 */

const delay = (ms: number): Promise<void> => new Promise(resolve => setTimeout(resolve, ms));

async function waitForElement(selector: string, timeout: number): Promise<Element> {
  return new Promise((resolve, reject) => {
    const intervalTime = 100;
    const endTime = Date.now() + timeout;
    const interval = setInterval(() => {
      const element = document.querySelector(selector);
      if (element) {
        clearInterval(interval);
        resolve(element);
      } else if (Date.now() > endTime) {
        clearInterval(interval);
        reject(new Error(`Element with selector "${selector}" not found within ${timeout}ms.`));
      }
    }, intervalTime);
  });
}

function setAndDispatchValue(element: HTMLTextAreaElement, text: string): void {
  // Ensure the element is indeed a textarea, as its 'value' property might not be writable directly on generic Element
  if (!(element instanceof HTMLTextAreaElement)) {
    console.warn("Attempted to set value on a non-HTMLTextAreaElement with setAndDispatchValue.", element);
    // Fallback or throw error as appropriate
    (element as HTMLInputElement).value = text; // Try as input element
  } else {
    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value")?.set;
    if (nativeInputValueSetter) {
      nativeInputValueSetter.call(element, text);
    } else {
      // Fallback if native setter is not found, though unlikely for HTMLTextAreaElement
      element.value = text;
    }
  }
  
  // Dispatch events to make sure frameworks like React detect the change
  element.dispatchEvent(new Event('input', { bubbles: true }));
  element.dispatchEvent(new Event('change', { bubbles: true }));
}

async function sendEnterKey(element: HTMLElement): Promise<void> {
  element.focus();
  if (element instanceof HTMLInputElement || element instanceof HTMLTextAreaElement) {
    element.select(); // Select the text, as suggested by user feedback
  }
  await delay(50); // Small delay after focus/select

  const commonEventProps: KeyboardEventInit = { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true, cancelable: true };
  
  element.dispatchEvent(new KeyboardEvent('keydown', commonEventProps));
  await delay(50); // Delay between key events
  element.dispatchEvent(new KeyboardEvent('keypress', commonEventProps));
  element.dispatchEvent(new KeyboardEvent('keyup', commonEventProps));
}

// Helper to click an element
function clickElement(element: HTMLElement | null): void {
  if (element) {
    element.click();
  }
}

// Helper to wait for text content of an element to change to an expected value
async function waitForElementTextContent(selector: string, expectedText: string, timeout: number = 5000): Promise<boolean> {
  const startTime = Date.now();
  return new Promise((resolve, reject) => {
    const interval = setInterval(() => {
      const element = document.querySelector(selector);
      if (element && element.textContent?.trim() === expectedText) {
        clearInterval(interval);
        resolve(true);
      } else if (Date.now() - startTime > timeout) {
        clearInterval(interval);
        reject(new Error(`Timed out waiting for element "${selector}" text to be "${expectedText}".`));
      }
    }, 100);
  });
}

interface ConnectionResult {
  success: boolean;
  reason?: string;
}

async function checkAndConnectBetaflight(): Promise<ConnectionResult> {
  const connectionButtonLabelSelector = '#header_buttons .connection_button .connection_button__label';
  const connectionButtonLinkSelector = '#header_buttons .connection_button .connection_button__link';
  
  let connectionLabel: Element;
  try {
    connectionLabel = await waitForElement(connectionButtonLabelSelector, 5000);
  } catch (error: any) {
    console.error("Connection label element not found:", error);
    return { success: false, reason: 'connection_label_not_found' };
  }

  const currentStatus = connectionLabel.textContent?.trim() || '';
  console.log("Current Betaflight connection status:", currentStatus);

  if (currentStatus === 'Connect') {
    console.log("Betaflight is disconnected. Attempting to connect...");
    const connectButton = document.querySelector<HTMLElement>(connectionButtonLinkSelector);
    if (!connectButton) {
      console.error("Connect button link not found.");
      return { success: false, reason: 'connect_button_not_found' };
    }
    clickElement(connectButton);
  } else if (currentStatus === 'Disconnect') {
    console.log("Betaflight is already connected.");
    return { success: true };
  } else if (currentStatus === 'Connecting') {
    console.log("Betaflight is currently connecting. Waiting for connection to establish...");
  } else {
    console.error("Invalid connection status encountered:", currentStatus);
    return { success: false, reason: 'invalid_connection_status' };
  }

  // Wait for the connection to be established (status changes to 'Disconnect')
  try {
    await waitForElementTextContent(connectionButtonLabelSelector, 'Disconnect', 10000);
    await delay(1000)
    console.log("Successfully connected to Betaflight.");
    return { success: true };
  } catch (error: any) {
    console.error("Failed to connect to Betaflight:", error);
    return { success: false, reason: 'connection_failed' };
  }
}

// Define a type for the message expected from chrome.runtime.onMessage
interface ChromeMessage {
  type: string;
  payload: {
    text: string;
  };
}

async function handleSetText(message: ChromeMessage, sendResponse: (response: { success: boolean; reason?: string }) => void): Promise<void> {
  const { text: userText } = message.payload;
  const textareaSelector = 'div.tab-cli textarea';
  const outputSelector = '.tab-cli .content_wrapper .backdrop .window .wrapper';

  // --- Check and Connect Betaflight ---
  const connectionResult = await checkAndConnectBetaflight();
  if (!connectionResult.success) {
    sendResponse({ success: false, reason: connectionResult.reason });
    return;
  }

  let textareaElement: HTMLTextAreaElement | null;
  try {
    textareaElement = document.querySelector<HTMLTextAreaElement>(textareaSelector);
    if (!textareaElement) {
      const cliTab = Array.from(document.querySelectorAll<HTMLElement>('div#tabs a')).find(a => a.textContent?.trim() === 'CLI');
      if (!cliTab) {
        sendResponse({ success: false, reason: 'cli_tab_not_found' });
        return;
      }
      cliTab.click();
      const awaitedElement = await waitForElement(textareaSelector, 2000);
      if (!(awaitedElement instanceof HTMLTextAreaElement)) {
        sendResponse({ success: false, reason: 'awaited_element_not_textarea' });
        return;
      }
      textareaElement = awaitedElement;
    }
  } catch (error: any) {
    sendResponse({ success: false, reason: 'textarea_not_found_after_click' });
    return;
  }

  const outputElement = document.querySelector<HTMLElement>(outputSelector);
  if (!outputElement) {
    sendResponse({ success: false, reason: 'output_element_not_found' });
    return;
  }

  // --- Readiness Check ---
  let isReady = false;
  const readinessCommand = "version";
  const expectedOutputSubstring = "Betaflight";

  // Clear the input before readiness check
  setAndDispatchValue(textareaElement, '');
  await sendEnterKey(textareaElement);
  await delay(200); // Wait for clear command to process

  for (let i = 0; i < 3; i++) {
    console.log(`Performing readiness check (attempt ${i + 1})...`);
    const textBefore = outputElement.textContent || '';
    
    setAndDispatchValue(textareaElement, readinessCommand);
    await sendEnterKey(textareaElement);

    await delay(1500); // Increased wait time

    const textAfter = outputElement.textContent || '';
    
    // Check if new text has appeared and contains the expected string
    if (textAfter.length > textBefore.length && textAfter.includes(expectedOutputSubstring)) {
      console.log("Terminal is ready.");
      isReady = true;
      // Clear the 'version' command from input
      setAndDispatchValue(textareaElement, '');
      await sendEnterKey(textareaElement);
      await delay(100);
      break;
    } else {
      const newText = textAfter.substring(textBefore.length);
      console.log(`Terminal not ready yet. New output: "${newText.replace(/\n/g, "\\n")}"`);
    }
  }

  if (isReady) {
    console.log("Setting and sending the final user text.");
    setAndDispatchValue(textareaElement, userText);
    await sendEnterKey(textareaElement);
    sendResponse({ success: true });
  } else {
    console.error("Terminal readiness check failed.");
    sendResponse({ success: false, reason: 'terminal_not_ready' });
  }
}

chrome.runtime.onMessage.addListener((message: ChromeMessage, _sender: chrome.runtime.MessageSender, sendResponse: (response: { success: boolean; reason?: string }) => void) => {
  if (message.type === 'SET_TEXT_IN_BETAFLIGHT_FIELD') {
    handleSetText(message, sendResponse).catch(err => {
        console.error("Unexpected error in Message Listener:", err);
        sendResponse({ success: false, reason: 'unknown_error' });
    });
    return true; // Async response
  }
});