<script>
  import ImageUpload from './ImageUpload.svelte';
  import ImageGallery from './ImageGallery.svelte';
  
  let images = [];
  
  const handleImagesUpdate = (newImages) => {
    images = newImages;
  };
</script>

<main>
  <h1>Image Upload App</h1>
  
  <ImageUpload bind:images />
  <ImageGallery {images} />
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
</style>