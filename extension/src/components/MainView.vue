<script setup lang="ts">
import {computed, onMounted, ref} from "vue";
import {useApiStore} from '../stores/apiStore';
import {PresetMetadata, PresetsCatalog, SearchFilter} from "../types.gen";
import {View} from "../types/view.ts";

const emit = defineEmits(['change-view']);

const apiStore = useApiStore();

const searchFilter = ref<SearchFilter>({
  id: -1,
  name: "Temporary Search Filter",
  search_query: "",
  author: "",
  tags: []
});

const areFiltersActive = computed(() => {
  return searchFilter.value.search_query.length > 0 || searchFilter.value.tags.length > 0 || searchFilter.value.author.length > 0;
});

function _filterCatalog(catalog: PresetsCatalog, filter: SearchFilter) {
  let authors: string[] = catalog.authors;
  if (filter.author) { // Authors are filtered
    // Yes, I know that this filtering can be done more efficiently
    authors = authors.filter(a => a.toLowerCase() === filter.author.toLowerCase())
  }

  let tags: string[] = catalog.tags;
  if (filter.tags.length > 0) { // Tags are filtered
    tags = tags.filter(t => filter.tags.includes(t));
  }

  let presets_metadata: PresetMetadata[] = catalog.presets_metadata.filter(p => {
    if (filter.search_query) { // Name is filtered
      if (!p.name.toLowerCase().includes(filter.search_query.toLowerCase())) return false;
    }

    if (filter.author) { // Author is filtered
      if (p.author.toLowerCase() !== filter.author.toLowerCase()) return false;
    }
    if (filter.tags) { // Tags are filtered
      if (!filter.tags.every(tag => p.tags.includes(tag))) return false;
    }
    return true;
  });

  return {
    presets_metadata: presets_metadata,
    authors: authors,
    tags: tags
  } as PresetsCatalog;
}

const filteredCatalog = computed<PresetsCatalog | null>(() => {
  if (!apiStore.catalog) return null;
  return _filterCatalog(apiStore.catalog, searchFilter.value)
})


onMounted(async () => { // TODO: Maybe init() function?
  await apiStore.loadApiUrl();
  await apiStore.loadCatalog();
});


function isTagSelectionValid(tag: string) {
  if (!apiStore.catalog) return false; // This function should not be called in this case anyway

  const filter: SearchFilter = JSON.parse(JSON.stringify(searchFilter.value));
  filter.tags.push(tag);
  const newCatalog = _filterCatalog(apiStore.catalog, filter);
  return newCatalog.presets_metadata.length > 0;
}

function toggleTag(tag: string) {
  const index = searchFilter.value.tags.indexOf(tag);
  if (index > -1) { // Tag is currently selected, so deselect it
    searchFilter.value.tags.splice(index, 1);
  } else { // Tag is not selected, so select it
    searchFilter.value.tags.push(tag);
  }
}

function selectPreset(id: number) {
  apiStore.selectPreset(id);
  changeView(View.PRESET);
}


function changeView(view: View) {
  emit("change-view", view);
}
</script>

<template>
  <div class="max-h-[450px] grid grid-rows-[auto,1fr] grid-cols-2 h-full gap-4">
    <!-- Row 1, Column 1: Filtered Presets Heading -->
    <h2 class="text-xl font-semibold text-gray-800">
      {{ areFiltersActive ? 'Filtered Presets' : 'Presets' }}
    </h2>

    <!-- Row 1, Column 2: Filter Options Heading -->
    <div class="flex justify-between items-center">
      <h3 class="text-lg font-semibold text-gray-800">Filter Options</h3>
      <button @click="changeView(View.SETTINGS)"
              class="text-gray-500 hover:text-gray-700 transition-colors duration-150">
        <img src="../../public/icons/settings.svg" alt="settings icon"
             style="width: 25px; height: 25px;"/>
      </button>
    </div>

    <!-- Row 2, Column 1: Filtered Catalog Content -->
    <div class="max-h-[400px] flex flex-col space-y-4 overflow-y-auto">
      <ul v-if="filteredCatalog" class="border border-gray-200 rounded-md flex-1 overflow-y-auto">
        <li v-for="p in filteredCatalog.presets_metadata" :key="p.id" @click="selectPreset(p.id)"
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

    <!-- Row 2, Column 2: Filtering Options Content -->
    <div class="h-[400px] flex flex-col space-y-4 overflow-hidden min-h-0">
      <!-- Search input (auto height) -->
      <div class="relative">
        <input
            type="text"
            v-model="searchFilter.search_query"
            placeholder="Search presets..."
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight
             focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent pr-10"/>
        <svg
            class="absolute right-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
          <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
        </svg>
      </div>

      <!-- Author filter (auto height) -->
      <div v-if="apiStore.catalog">
        <h4 class="text-md font-semibold text-gray-700 mb-2">Filter by Author:</h4>
        <div class="relative">
          <select
              v-model="searchFilter.author"
              class="block appearance-none w-full bg-white border border-gray-200 text-gray-700
               py-2 px-3 pr-8 rounded leading-tight focus:outline-none focus:bg-white
               focus:border-gray-500 shadow">
            <option value="">All authors</option>
            <option v-for="author in apiStore.catalog.authors" :key="author" :value="author">
              {{ author }}
            </option>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <svg
                class="fill-current h-4 w-4"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20">
              <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Tags: fills remaining space and scrolls -->
      <div v-if="apiStore.catalog" class="flex flex-col flex-1 min-h-0">
        <h4 class="text-md font-semibold text-gray-700 mb-2">Filter by Tags:</h4>

        <div
            v-if="apiStore.catalog.tags.length > 0"
            class="relative py-2 border-t border-gray-200 flex-1 overflow-y-auto min-h-0">
          <div
              ref="tagsContainer"
              class="flex flex-wrap gap-2">
            <span
                v-for="tag in apiStore.catalog.tags"
                :key="tag"
                :class="[
                'px-3 py-1 rounded-full text-sm transition-colors duration-150',
                searchFilter.tags.includes(tag)
                  ? 'bg-blue-600 text-white cursor-pointer'
                  : isTagSelectionValid(tag)
                    ? 'bg-gray-200 text-gray-700 hover:bg-gray-300 cursor-pointer'
                    : 'bg-gray-100 text-gray-400 opacity-50 cursor-not-allowed'
                ]"
                @click="isTagSelectionValid(tag) ? toggleTag(tag) : undefined">
              {{ tag }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>