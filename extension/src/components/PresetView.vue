<script setup lang="ts">
import { computed, onMounted, watch } from 'vue';
import { useApiStore } from '../stores/apiStore';

const apiStore = useApiStore();

const preset = computed(() => apiStore.selectedPresetDetails);

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
  }
});

function goBack() {
  apiStore.selectedPresetId = null; // Clear selected preset to go back to MainView
  apiStore.selectedPresetDetails = null; // Clear details
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
        <!-- Add more details as needed -->
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
