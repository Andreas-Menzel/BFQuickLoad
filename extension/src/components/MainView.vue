<script setup lang="ts">
import {computed, onMounted, ref} from "vue";
import {useApiStore} from '../stores/apiStore';
import {PresetMetadata} from "../types"; // Assuming PresetMetadata has a 'tags' property

const emit = defineEmits(['change-view']); // Declare emits

const searchQuery = ref<string>("");
const selectedTags = ref<string[]>([]); // New state for selected tags
const selectedAuthors = ref<string[]>([]); // New state for selected authors
const isTagsExpanded = ref(false); // State for tags section expansion
const tagsContainer = ref<HTMLElement | null>(null); // Reference to the tags container div
const maxTagsHeight = 150; // Max height in pixels for collapsed tags

const isAuthorsExpanded = ref(false); // State for authors section expansion
const authorsContainer = ref<HTMLElement | null>(null); // Reference to the authors container div
const maxAuthorsHeight = 150; // Max height in pixels for collapsed authors

const apiStore = useApiStore();

// Computed property to get all unique tags from the catalog
const allTags = computed<string[]>(() => {
  const tags = new Set<string>();
  apiStore.catalog.forEach((preset: PresetMetadata) => {
    preset.tags?.forEach(tag => tags.add(tag));
  });
  return Array.from(tags).sort();
});

// Computed property to get all unique authors from the catalog
const allAuthors = computed<string[]>(() => {
  const authors = new Set<string>();
  apiStore.catalog.forEach((preset: PresetMetadata) => {
    if (preset.author) {
      authors.add(preset.author);
    }
  });
  return Array.from(authors).sort();
});



const areFiltersActive = computed(() => {
  return searchQuery.value.length > 0 || selectedTags.value.length > 0 || selectedAuthors.value.length > 0;
});

const filteredCatalog = computed(() => {
  return apiStore.catalog.filter(p => {
    const matchesSearchQuery = p.name.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesSelectedTags = selectedTags.value.length === 0 ||
        (p.tags && selectedTags.value.every(selectedTag => p.tags.includes(selectedTag)));
    const matchesSelectedAuthors = selectedAuthors.value.length === 0 ||
        (p.author && selectedAuthors.value.includes(p.author));

    return matchesSearchQuery && matchesSelectedTags && matchesSelectedAuthors;
  })
})

const isTagSelectable = computed(() => (tag: string) => {
  if (selectedTags.value.includes(tag)) {
    return true; // Already selected tags are always selectable (to deselect them)
  }

  // Check if adding this tag would result in any presets
  const hypotheticalSelectedTags = [...selectedTags.value, tag];
  const matchingPresets = apiStore.catalog.filter(p => {
    const matchesSearchQuery = p.name.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesSelectedAuthors = selectedAuthors.value.length === 0 ||
        (p.author && selectedAuthors.value.includes(p.author));
    return matchesSearchQuery && matchesSelectedAuthors && p.tags && hypotheticalSelectedTags.every(selectedTag => p.tags.includes(selectedTag));
  });
  return matchingPresets.length > 0;
});

const isAuthorSelectable = computed(() => (author: string) => {
  if (selectedAuthors.value.includes(author)) {
    return true; // Already selected authors are always selectable (to deselect them)
  }

  const hypotheticalSelectedAuthors = [...selectedAuthors.value, author];
  const matchingPresets = apiStore.catalog.filter(p => {
    const matchesSearchQuery = p.name.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesSelectedTags = selectedTags.value.length === 0 ||
        (p.tags && selectedTags.value.every(selectedTag => p.tags.includes(selectedTag)));
    return matchesSearchQuery && matchesSelectedTags && p.author && hypotheticalSelectedAuthors.includes(p.author);
  });
  return matchingPresets.length > 0;
});

// Determine if the "Show More/Less" button should be visible for tags
const showExpandButton = computed(() => {
  if (tagsContainer.value) {
    return tagsContainer.value.scrollHeight > maxTagsHeight;
  }
  return false;
});

// Determine if the "Show More/Less" button should be visible for authors
const showAuthorExpandButton = computed(() => {
  if (authorsContainer.value) {
    return authorsContainer.value.scrollHeight > maxAuthorsHeight;
  }
  return false;
});

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
    // Tag is currently selected, so deselect it
    selectedTags.value.splice(index, 1);
  } else {
    // Tag is not selected, try to select it if it's selectable
    if (isTagSelectable.value(tag)) {
      selectedTags.value.push(tag);
    }
  }
}

function toggleAuthor(author: string) {
  const index = selectedAuthors.value.indexOf(author);
  if (index > -1) {
    selectedAuthors.value.splice(index, 1); // Deselect author
  } else {
    if (isAuthorSelectable.value(author)) {
      selectedAuthors.value.push(author); // Select author if selectable
    }
  }
}

function toggleTagsExpansion() {
  isTagsExpanded.value = !isTagsExpanded.value;
}

function toggleAuthorsExpansion() {
  isAuthorsExpanded.value = !isAuthorsExpanded.value;
}

function goToSettings() {
  emit('change-view', 'settings');
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
      <button @click="goToSettings" class="text-gray-500 hover:text-gray-700 transition-colors duration-150">
        <img src="../../public/icons/settings.svg" alt="settings icon"
             style="width: 25px; height: 25px;"/>
      </button>
    </div>

    <!-- Row 2, Column 1: Filtered Catalog Content -->
    <div class="flex flex-col space-y-4 overflow-y-auto">
      <ul v-if="filteredCatalog.length > 0" class="border border-gray-200 rounded-md flex-1 overflow-y-auto">
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

    <!-- Row 2, Column 2: Filtering Options Content -->
    <div class="flex flex-col space-y-4 overflow-y-auto">
      <div class="relative">
        <input type="text" v-model="searchQuery" placeholder="Search presets..."
               class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent pr-10"/>
        <svg class="absolute right-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" fill="none" stroke="currentColor"
             viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
        </svg>
      </div>

      <div>
        <h4 class="text-md font-semibold text-gray-700 mb-2">Filter by Author:</h4>
        <div v-if="allAuthors.length > 0" class="relative py-2 border-t border-b border-gray-200">
          <div ref="authorsContainer"
               :class="{'max-h-[150px] overflow-hidden': !isAuthorsExpanded, 'transition-max-height duration-500 ease-in-out': true}"
               class="flex flex-wrap gap-2">
            <span v-for="author in allAuthors" :key="author"
                  :class="[
                    'px-3 py-1 rounded-full text-sm transition-colors duration-150 cursor-pointer', // Always cursor-pointer
                    selectedAuthors.includes(author)
                      ? 'bg-blue-600 text-white' // Active author style
                      : isAuthorSelectable(author)
                        ? 'bg-gray-200 text-gray-700 hover:bg-gray-300' // Inactive but selectable
                        : 'bg-gray-100 text-gray-400 opacity-50' // Disabled author style
                  ]"
                  @click="toggleAuthor(author)">
              {{ author }}
            </span>
          </div>
          <div v-if="!isAuthorsExpanded && showAuthorExpandButton"
               class="absolute bottom-4 left-0 w-full h-12 bg-gradient-to-t from-white to-white/0 pointer-events-none"></div>
          <button v-if="showAuthorExpandButton" @click="toggleAuthorsExpansion"
                  class="mt-2 w-full text-center text-blue-600 hover:text-blue-800 text-sm font-semibold transition-colors duration-150 opacity-100 relative z-10">
            {{ isAuthorsExpanded ? 'Show Less' : 'Show More' }}
          </button>
        </div>
      </div>

      <div>
        <h4 class="text-md font-semibold text-gray-700 mb-2">Filter by Tags:</h4>
        <div v-if="allTags.length > 0" class="relative py-2 border-t border-gray-200">
          <div ref="tagsContainer"
               :class="{'max-h-[150px] overflow-hidden': !isTagsExpanded, 'transition-max-height duration-500 ease-in-out': true}"
               class="flex flex-wrap gap-2">
            <span v-for="tag in allTags" :key="tag"
                  :class="[
                    'px-3 py-1 rounded-full text-sm transition-colors duration-150 cursor-pointer', // Always cursor-pointer
                    selectedTags.includes(tag)
                      ? 'bg-blue-600 text-white' // Active tag style
                      : isTagSelectable(tag)
                        ? 'bg-gray-200 text-gray-700 hover:bg-gray-300' // Inactive but selectable
                        : 'bg-gray-100 text-gray-400 opacity-50' // Disabled tag style
                  ]"
                  @click="toggleTag(tag)">
              {{ tag }}
            </span>
          </div>
          <div v-if="!isTagsExpanded && showExpandButton"
               class="absolute bottom-4 left-0 w-full h-12 bg-gradient-to-t from-white to-white/0 pointer-events-none"></div>
          <button v-if="showExpandButton" @click="toggleTagsExpansion"
                  class="mt-2 w-full text-center text-blue-600 hover:text-blue-800 text-sm font-semibold transition-colors duration-150 opacity-100 relative z-10">
            {{ isTagsExpanded ? 'Show Less' : 'Show More' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.transition-max-height {
  transition-property: max-height;
}
</style>