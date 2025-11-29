import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { DefaultService } from '../types'; // Added
import { OpenAPI, Preset, PresetMetadata } from '../types'; // Modified

export const useApiStore = defineStore('api', () => {
  const apiUrl = ref<string>("");
  const chromeStorageApiUrl = ref<string>(""); // To keep track of the URL in Chrome Storage
  const catalog = ref<PresetMetadata[]>([]); // New state for catalog
  const selectedPresetId = ref<string | null>(null); // New state for selected preset ID
  const selectedPresetDetails = ref<Preset | null>(null); // New state for selected preset details

  const isApiUrlSet = computed(() => !!apiUrl.value);

  async function loadApiUrl() {
    const result = await chrome.storage.local.get(["apiUrl"]);
    const storedUrl = result["apiUrl"];
    if (typeof storedUrl === 'string') {
      apiUrl.value = storedUrl;
      chromeStorageApiUrl.value = storedUrl;
      OpenAPI.BASE = storedUrl; // Set OpenAPI.BASE on load
    } else {
        apiUrl.value = "http://127.0.0.1:8000"
        OpenAPI.BASE = apiUrl.value; // Set OpenAPI.BASE on load
    }
  }

  async function saveApiUrl(newUrl: string) {
    apiUrl.value = newUrl;
    await chrome.storage.local.set({["apiUrl"]: apiUrl.value});
    chromeStorageApiUrl.value = apiUrl.value;
    OpenAPI.BASE = newUrl; // Set OpenAPI.BASE on save
  }

  // New action to load the catalog
  async function loadCatalog() {
    if (!isApiUrlSet.value) {
      console.error("API URL is not set. Cannot load catalog.");
      return;
    }
    try {
      catalog.value = await DefaultService.getCatalog();
    } catch (error) {
      console.error("Failed to load catalog:", error);
      catalog.value = [];
    }
  }

  // New action to load full preset details
  async function loadPresetDetails(presetId: number) {
    if (!isApiUrlSet.value) {
      console.error("API URL is not set. Cannot load preset details.");
      return null;
    }
    try {
      selectedPresetDetails.value = await DefaultService.getPreset(presetId);
      return selectedPresetDetails.value;
    } catch (error) {
      console.error(`Failed to load preset details for ID ${presetId}:`, error);
      selectedPresetDetails.value = null;
      return null;
    }
  }

  // New action to select a preset
  async function selectPreset(presetId: number) {
    selectedPresetId.value = presetId.toString(); // Store as string if needed elsewhere, but pass number to getPreset
    await loadPresetDetails(presetId);
  }

  // Expose DefaultService through the store
  const apiService = DefaultService;

  return {
    apiUrl,
    chromeStorageApiUrl,
    isApiUrlSet,
    catalog,
    selectedPresetId,
    selectedPresetDetails,
    loadApiUrl,
    saveApiUrl,
    loadCatalog,
    loadPresetDetails,
    selectPreset,
    apiService,
  };
});

