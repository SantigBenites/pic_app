<script>
  import Upload from './ImageUpload.svelte';
  import Gallery from './ImageGallery.svelte';
  
  let currentView = 'upload'; // 'upload' or 'gallery'
</script>

<main>
  <h1>Image Upload App</h1>
  <nav>
    <button on:click={() => currentView = 'upload'}>Upload</button>
    <button on:click={() => currentView = 'gallery'}>Gallery</button>
  </nav>
  
  {#if currentView === 'upload'}
    <Upload />
  {:else if currentView === 'gallery'}
    <Gallery />
  {/if}
</main>

<style>
  main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  h1 {
    text-align: center;
    color: #333;
  }
  nav {
    text-align: center;
    margin: 20px 0;
    padding: 10px;
  }
  button {
    background: none;
    border: none;
    color: #4CAF50;
    text-decoration: none;
    font-weight: bold;
    padding: 5px 10px;
    cursor: pointer;
    font-size: 1em;
  }
  button:hover {
    text-decoration: underline;
  }
</style>