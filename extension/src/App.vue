<script setup lang="ts">
import {ref} from 'vue'
import MainView from './components/MainView.vue'
import SettingsView from './components/SettingsView.vue'
import PresetView from './components/PresetView.vue'
import {View} from "./types/view.ts";

const currentView = ref<View>(View.MAIN);

function handleViewChange(view: View) {
  currentView.value = view;
}
</script>

<template>
  <div class="app w-[580px] p-4 bg-gray-50 flex flex-col space-y-4">
    <h1 class="text-2xl font-bold text-gray-800 text-center mb-4">BFQuickLoad</h1>

    <div class="mt-4">
      <MainView v-if="currentView === View.MAIN"
                @change-view="handleViewChange"/>
      <SettingsView v-else-if="currentView === View.SETTINGS"
                    @change-view="handleViewChange"/>
      <PresetView v-else-if="currentView === View.PRESET"
                  @change-view="handleViewChange"/>
    </div>
  </div>
</template>

<style scoped>
.app {
  transition: height 1s;
}
</style>