<script setup lang="ts">
import {onMounted, ref} from 'vue'
import { useApiStore } from '../stores/apiStore';
import {DefaultService} from "../types";

const emit = defineEmits(['change-view']); // Declare emits

const apiStore = useApiStore();

const connectionStatus = ref<"connected" | "disconnected" | null>(null);

async function saveApiUrlWrapper() {
  await apiStore.saveApiUrl(apiStore.apiUrl);
  connectionStatus.value = null; // Reset connection status after saving
}

async function testConnection() {
  connectionStatus.value = null; // Clear previous status

  if (!apiStore.apiUrl) {
    console.error("API URL is not set.");
    connectionStatus.value = "disconnected";
    return;
  }

  try {
    const data = await DefaultService.ping();

    if (data && data.app_name === "BFQuickLoad") {
      connectionStatus.value = "connected";
    } else {
      connectionStatus.value = "disconnected";
    }
  } catch (error) {
    console.error("Connection test failed:", error);
    connectionStatus.value = "disconnected";
  }
}

onMounted(async () => {
  await apiStore.loadApiUrl();
});

function closeSettings() {
  emit('change-view', 'main');
}
</script>

<template>
  <div class="space-y-4">
    <div class="flex justify-between items-center">
      <h2 class="text-xl font-semibold text-gray-800">Settings</h2>
      <button @click="closeSettings" class="text-gray-500 hover:text-gray-700 transition-colors duration-150">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
    <div>
      <label for="apiUrl" class="block text-gray-700 text-sm font-semibold mb-2">
        API URL:
      </label>
      <input
          type="text"
          id="apiUrl"
          v-model="apiStore.apiUrl"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          placeholder="e.g., http://127.0.0.1:8000"
      />
      <div class="mt-2 text-sm">
        <p v-if="connectionStatus === 'disconnected'" class="text-red-600">Connection could not be established. Is the URL correct and the
          server running?</p>
        <p v-else-if="connectionStatus === 'connected'" class="text-green-600">Connection established. Happy tuning!</p>
      </div>
    </div>
    <div class="flex space-x-2">
      <button @click="saveApiUrlWrapper" :disabled="apiStore.apiUrl === apiStore.chromeStorageApiUrl"
              class="flex-1 px-4 py-2 rounded-md font-semibold transition-colors duration-200 bg-blue-600 text-white shadow-sm hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed">
        Save
      </button>
      <button @click="testConnection"
              class="flex-1 px-4 py-2 rounded-md font-semibold transition-colors duration-200 bg-gray-200 text-gray-700 shadow-sm hover:bg-gray-300">
        Test Connection
      </button>
    </div>

    <hr class="my-4">

    <div class="grid grid-cols-2 gap-4 mt-4 items-center">
      <div class="flex justify-center">
        <img src="/logo128.png" alt="BFQuickLoad Logo" class="h-32 w-auto">
      </div>

      <div class="text-gray-500 text-sm">
        <p>Developed by Andreas Menzel</p>
        <p>
          <a href="https://github.com/Andreas-Menzel/BFQuickLoad" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:underline">
            GitHub Repository
          </a>
        </p>
        <p class="mt-2">
          Join the
          <a href="https://www.instagram.com/FPVonSpot" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:underline">
            FPVonSpot
          </a>
          crew!
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>