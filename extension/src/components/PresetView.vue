<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue';
import { useApiStore } from '../stores/apiStore';

const apiStore = useApiStore();

const preset = computed(() => apiStore.selectedPresetDetails);
const statusMessage = ref<string | null>(null);
const isSending = ref<boolean>(false);

// Optional: Load details if selectedPresetId is set but details are not loaded (e.g., direct navigation)
onMounted(() => {
  if (apiStore.selectedPresetId && !preset.value) {
    apiStore.loadPresetDetails(parseInt(apiStore.selectedPresetId));
  }
});

// Watch for changes in selectedPresetId to load new details
watch(() => apiStore.selectedPresetId, (newId) => {
  if (newId) {
    apiStore.loadPresetDetails(parseInt(newId));
    statusMessage.value = null; // Clear status when a new preset is selected
  }
});

function goBack() {
  apiStore.selectedPresetId = null; // Clear selected preset to go back to MainView
  apiStore.selectedPresetDetails = null; // Clear details
  statusMessage.value = null; // Clear status
}

async function sendPresetToCli() {
  if (!preset.value || !preset.value.content) {
    statusMessage.value = "Error: Preset content is missing.";
    return;
  }

  isSending.value = true;
  statusMessage.value = "Sending command...";
  const result = await apiStore.sendCommandToBetaflight(preset.value.content);
  isSending.value = false;

  if (result.success) {
    statusMessage.value = "Command sent successfully!";
  } else {
    let errorMessage = "Failed to send command.";
    switch (result.reason) {
      case 'no_active_tab':
        errorMessage = 'Error: No active tab found.';
        break;
      case 'cli_tab_not_found':
        errorMessage = 'Error: "CLI" tab not found in Betaflight configurator.';
        break;
      case 'textarea_not_found_after_click':
        errorMessage = 'Error: CLI input field not found after switching to CLI tab.';
        break;
      case 'output_element_not_found':
        errorMessage = 'Error: Betaflight output element not found.';
        break;
      case 'terminal_not_ready':
        errorMessage = 'Error: Betaflight terminal not ready after multiple attempts.';
        break;
      case 'unknown_error':
        errorMessage = 'An unknown error occurred while sending the command.';
        break;
      default:
        errorMessage = `Failed to send command: ${result.reason || 'unknown reason'}.`;
        break;
    }
    statusMessage.value = errorMessage;
  }
}
</script>

<template>
  <div class="space-y-4">
    <div v-if="preset">
      <h2 class="text-xl font-semibold text-gray-800 mb-2">{{ preset.name }}</h2>
      <div class="text-gray-700 space-y-1">
        <p><strong>Author:</strong> {{ preset.author }}</p>
        <p><strong>Description:</strong> {{ preset.description }}</p>
        <p v-if="preset.tags && preset.tags.length"><strong>Tags:</strong>
          <span v-for="tag in preset.tags" :key="tag"
                class="inline-block bg-blue-100 text-blue-800 text-xs px-2 rounded-full mr-1">
            {{ tag }}
          </span>
        </p>
        <p class="font-mono bg-gray-100 p-2 rounded text-sm mt-2 max-h-40 overflow-y-auto whitespace-pre-wrap">
          {{ preset.content }}
        </p>
      </div>
      
      <div class="mt-4">
        <button @click="sendPresetToCli" :disabled="isSending"
                class="w-full px-4 py-2 rounded-md font-semibold transition-colors duration-200 bg-blue-600 text-white shadow-sm hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed">
          <span v-if="isSending">Sending...</span>
          <span v-else>Send to Betaflight CLI</span>
        </button>
        <p v-if="statusMessage" :class="{'text-green-600': statusMessage.includes('successfully'), 'text-red-600': statusMessage.includes('Error') || statusMessage.includes('Failed')}" class="mt-2 text-sm text-center">
          {{ statusMessage }}
        </p>
      </div>

    </div>
    <div v-else class="text-gray-600">
      <p>Loading preset details or no preset selected...</p>
    </div>

    <button @click="goBack"
            class="w-full px-4 py-2 rounded-md font-semibold transition-colors duration-200 bg-gray-200 text-gray-700 shadow-sm hover:bg-gray-300">
      Back to Catalog
    </button>
  </div>
</template>

<style scoped>
/* Add any specific styles for PresetView here */
</style>
