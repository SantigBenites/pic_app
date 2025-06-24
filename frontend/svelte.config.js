import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
  kit: {
    files: {
      routes: 'src/routes' // or your custom directory
    }
  },
  preprocess: vitePreprocess()
};

export default config;
