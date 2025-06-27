<script>
  import { page } from '$app/stores';
  import Upload from '$pages/ImageUpload.svelte';
  import Gallery from '$pages/ImageGallery.svelte';
  
  $: currentPath = $page.url.pathname;
</script>

{#if currentPath === '/upload'}
  <Upload />
{:else if currentPath === '/gallery'}
  <Gallery />
{/if}