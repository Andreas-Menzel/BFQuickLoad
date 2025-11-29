<template>
  <div class="w-80 h-auto p-4 bg-gray-50 flex flex-col space-y-4">
    <h1 class="text-2xl font-bold text-gray-800 text-center mb-4">BFQuickLoad</h1>

    <div class="mt-4">
      <PresetView v-if="showPresetView" />
      <MainView v-else-if="currentView === 'main'" @change-view="handleViewChange" />
      <SettingsView v-else-if="currentView === 'settings'" @change-view="handleViewChange" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import MainView from './components/MainView.vue'
import SettingsView from './components/SettingsView.vue'
import PresetView from './components/PresetView.vue'
import { useApiStore } from './stores/apiStore'

const currentView = ref<'main' | 'settings'>('main')
const apiStore = useApiStore();

const showPresetView = computed(() => !!apiStore.selectedPresetId);

function handleViewChange(view: 'main' | 'settings') {
  currentView.value = view;
}
</script>

<style scoped>
/* No specific styles needed, Tailwind handles it */
</style>