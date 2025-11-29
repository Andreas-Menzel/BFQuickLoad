<script setup lang="ts">
import {computed, onMounted, ref} from "vue";
import {useApiStore} from '../stores/apiStore';
import {PresetMetadata} from "../types"; // Assuming PresetMetadata has a 'tags' property

const emit = defineEmits(['change-view']); // Declare emits

const searchQuery = ref<string>("");
const selectedTags = ref<string[]>([]); // New state for selected tags

const apiStore = useApiStore();

// Computed property to get all unique tags from the catalog
const allTags = computed<string[]>(() => {
  const tags = new Set<string>();
  apiStore.catalog.forEach((preset: PresetMetadata) => {
    preset.tags?.forEach(tag => tags.add(tag));
  });
  return Array.from(tags).sort();
});

const filteredCatalog = computed(() => {
  return apiStore.catalog.filter(p => {
    const matchesSearchQuery = p.name.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesSelectedTags = selectedTags.value.length === 0 ||
        (p.tags && selectedTags.value.every(selectedTag => p.tags.includes(selectedTag)));
    return matchesSearchQuery && matchesSelectedTags;
  })
})

onMounted(async () => {
  await apiStore.loadApiUrl();
  await apiStore.loadCatalog();
});

function selectPreset(id: number) {
  apiStore.selectPreset(id);
}

function toggleTag(tag: string) {
  const index = selectedTags.value.indexOf(tag);
  if (index > -1) {
    selectedTags.value.splice(index, 1); // Remove tag
  } else {
    selectedTags.value.push(tag); // Add tag
  }
}

function goToSettings() {
  emit('change-view', 'settings');
}
</script>

<template>
  <div class="space-y-4">
    <div class="flex justify-between items-center">
      <h2 class="text-xl font-semibold text-gray-800">Catalog</h2>
      <button @click="goToSettings" class="text-gray-500 hover:text-gray-700 transition-colors duration-150">
        <img src="../../public/icons/settings.svg" alt="settings icon"
             style="width: 25px; height: 25px;"/>
      </button>
    </div>

    <div class="relative">
      <input type="text" v-model="searchQuery" placeholder="Search presets..."
             class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent pr-10"/>
      <svg class="absolute right-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" fill="none" stroke="currentColor"
           viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
      </svg>
    </div>

    <div v-if="allTags.length > 0" class="flex flex-wrap gap-2 py-2 border-t border-b border-gray-200">
      <span v-for="tag in allTags" :key="tag" @click="toggleTag(tag)"
            :class="[
              'px-3 py-1 rounded-full text-sm cursor-pointer transition-colors duration-150',
              selectedTags.includes(tag) ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            ]">
        {{ tag }}
      </span>
    </div>

    <ul v-if="filteredCatalog.length > 0" class="border border-gray-200 rounded-md max-h-60 overflow-y-auto">
      <li v-for="p in filteredCatalog" :key="p.id" @click="selectPreset(p.id)"
          class="px-4 py-2 cursor-pointer hover:bg-blue-50 transition-colors duration-150 text-gray-800 border-b border-gray-100 last:border-b-0">
        {{ p.name }}
      </li>
    </ul>
    <p v-else class="text-gray-600 text-center py-4">No presets found.</p>

    <button @click="apiStore.loadCatalog" :disabled="!apiStore.isApiUrlSet"
            class="w-full px-4 py-2 rounded-md font-semibold transition-colors duration-200 bg-blue-600 text-white shadow-sm hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed">
      Reload Catalog
    </button>
  </div>
</template>

<style scoped>
/* No specific styles needed, Tailwind handles it */
</style>