/**
 * content.js
 * Version mit robusterer Event-Simulation, Bereitschaftsprüfung und Verbindungsmanagement.
 */

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

function waitForElement(selector, timeout) {
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

function setAndDispatchValue(element, text) {
  const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
  nativeInputValueSetter.call(element, text);
  
  // Dispatch events to make sure frameworks like React detect the change
  element.dispatchEvent(new Event('input', { bubbles: true }));
  element.dispatchEvent(new Event('change', { bubbles: true }));
}

async function sendEnterKey(element) {
  element.focus();
  element.select(); // Select the text, as suggested by user feedback
  await delay(50); // Small delay after focus/select

  const commonEventProps = { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true, cancelable: true };
  
  element.dispatchEvent(new KeyboardEvent('keydown', commonEventProps));
  await delay(50); // Delay between key events
  element.dispatchEvent(new KeyboardEvent('keypress', commonEventProps));
  element.dispatchEvent(new KeyboardEvent('keyup', commonEventProps));
}

// Helper to click an element
function clickElement(element) {
  if (element) {
    element.click();
  }
}

// Helper to wait for text content of an element to change to an expected value
async function waitForElementTextContent(selector, expectedText, timeout = 5000) {
  const startTime = Date.now();
  return new Promise((resolve, reject) => {
    const interval = setInterval(() => {
      const element = document.querySelector(selector);
      if (element && element.textContent.trim() === expectedText) {
        clearInterval(interval);
        resolve(true);
      } else if (Date.now() - startTime > timeout) {
        clearInterval(interval);
        reject(new Error(`Timed out waiting for element "${selector}" text to be "${expectedText}".`));
      }
    }, 100);
  });
}


async function checkAndConnectBetaflight() {
  const connectionButtonLabelSelector = '#header_buttons .connection_button .connection_button__label';
  const connectionButtonLinkSelector = '#header_buttons .connection_button .connection_button__link';
  
  let connectionLabel;
  try {
    connectionLabel = await waitForElement(connectionButtonLabelSelector, 5000);
  } catch (error) {
    console.error("Connection label element not found:", error);
    return { success: false, reason: 'connection_label_not_found' };
  }

  const currentStatus = connectionLabel.textContent.trim();
  console.log("Current Betaflight connection status:", currentStatus);

  if (currentStatus === 'Connect') {
    console.log("Betaflight is disconnected. Attempting to connect...");
    const connectButton = document.querySelector(connectionButtonLinkSelector);
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
    await waitForElementTextContent(connectionButtonLabelSelector, 'Disconnect', 10000); // Wait up to 15 seconds for connection
      await delay(1000)
    console.log("Successfully connected to Betaflight.");
    return { success: true };
  } catch (error) {
    console.error("Failed to connect to Betaflight:", error);
    return { success: false, reason: 'connection_failed' };
  }
}


async function handleSetText(message, sendResponse) {
  const { text: userText } = message.payload;
  const textareaSelector = 'div.tab-cli textarea';
  const outputSelector = '.tab-cli .content_wrapper .backdrop .window .wrapper';

  // --- Check and Connect Betaflight ---
  const connectionResult = await checkAndConnectBetaflight();
  if (!connectionResult.success) {
    sendResponse({ success: false, reason: connectionResult.reason });
    return;
  }

  let textareaElement;
  try {
    textareaElement = document.querySelector(textareaSelector);
    if (!textareaElement) {
      const cliTab = Array.from(document.querySelectorAll('div#tabs a')).find(a => a.textContent.trim() === 'CLI');
      if (!cliTab) {
        sendResponse({ success: false, reason: 'cli_tab_not_found' });
        return;
      }
      cliTab.click();
      textareaElement = await waitForElement(textareaSelector, 2000);
    }
  } catch (error) {
    sendResponse({ success: false, reason: 'textarea_not_found_after_click' });
    return;
  }

  const outputElement = document.querySelector(outputSelector);
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
    const textBefore = outputElement.textContent;
    
    setAndDispatchValue(textareaElement, readinessCommand);
    await sendEnterKey(textareaElement);

    await delay(1500); // Increased wait time

    const textAfter = outputElement.textContent;
    
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

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'SET_TEXT_IN_BETAFLIGHT_FIELD') {
    handleSetText(message, sendResponse).catch(err => {
        console.error("Unexpected error in Message Listener:", err);
        sendResponse({ success: false, reason: 'unknown_error' });
    });
    return true; // Async response
  }
});
