# Chrome Extension with Vue 3, TypeScript, and Tailwind CSS

This is a minimal Chrome Extension project scaffold demonstrating the integration of Vue 3 (Composition API with `<script setup>`), TypeScript, and Tailwind CSS using Vite for building. The extension uses Manifest V3.

## Project Overview

-   **Frontend Framework**: Vue 3 with Composition API (`<script setup lang="ts">`)
-   **Language**: TypeScript
-   **Styling**: Tailwind CSS
-   **Build Tool**: Vite
-   **Extension Manifest**: Manifest V3
-   **Functionality**: A browser action popup with two views (Main and Settings) that can be toggled.

## Prerequisites

-   Node.js (LTS recommended)
-   npm (comes with Node.js)

## Installation

1.  Navigate into the `extension` directory:
    ```bash
    cd extension
    ```
2.  Install the project dependencies:
    ```bash
    npm install
    ```

## Building the Project

To build the extension for production:

```bash
npm run build
```

This command will compile the Vue application, TypeScript, and Tailwind CSS into the `dist/` directory.

## Loading the Extension in Chrome

1.  Open Chrome and navigate to `chrome://extensions`.
2.  Enable "Developer mode" by toggling the switch in the top right corner.
3.  Click on the "Load unpacked" button.
4.  Select the `dist/` directory inside your `extension` folder (e.g., `/path/to/BFQuickLoad/extension/dist`).
5.  The extension should now be loaded and visible in your browser's extension toolbar. Click its icon to open the popup.

## How it's Wired Together

-   `manifest.json`: Defines the extension's properties, including the `popup.html` as the default browser action popup.
-   `popup.html`: The entry HTML file for the popup. It includes a `<div id="app"></div>` where the Vue application is mounted and loads `src/main.ts` as a module script.
-   `src/main.ts`: The main TypeScript entry point. It bootstraps the Vue application by creating a Vue app from `src/App.vue` and mounting it to the `#app` element. It also imports `src/assets/tailwind.css`.
-   `src/assets/tailwind.css`: Contains the Tailwind CSS directives (`@tailwind base;`, `@tailwind components;`, `@tailwind utilities;`). PostCSS processes this file to generate the final CSS.
-   `src/App.vue`: The root Vue component for the popup. It manages the state for `currentView` and conditionally renders `MainView.vue` or `SettingsView.vue`. It also demonstrates using Tailwind CSS for styling buttons and layout.
-   `src/components/MainView.vue` and `src/components/SettingsView.vue`: Simple Vue components using `<script setup lang="ts">` and Tailwind CSS classes for basic styling and content.
-   `tailwind.config.js`: Configures Tailwind CSS, specifying which files to scan for classes (`content` array).
-   `postcss.config.js`: Integrates Tailwind CSS and Autoprefixer into the PostCSS processing pipeline.
-   `vite.config.ts`: Configures Vite to build the project. Specifically, `rollupOptions.input.popup` ensures `popup.html` is handled, and `output` settings format the build for extension loading.
-   `tsconfig.json`: TypeScript configuration for the project.

## Extending the UI and Logic

-   **Popup UI**: Modify `src/App.vue` to add more navigation, or create new components in `src/components/` and import them into `App.vue` or other components.
-   **Styles**: Continue using Tailwind CSS classes directly in your Vue templates. For custom CSS, you can add new `.css` files and import them, or use `<style scoped>` within Vue components.
-   **Background Scripts/Content Scripts**: For more complex extension functionality, you would add `background.ts` or `content.ts` files and declare them in `manifest.json`. You would also need to update `vite.config.ts` to include these as additional entry points in the build process.
-   **State Management**: For more complex state management, consider libraries like Pinia (the official Vuex successor).
