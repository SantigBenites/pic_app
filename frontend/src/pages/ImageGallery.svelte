<script>
  import axios from 'axios';
  import { onMount } from 'svelte';

  let images = [];
  let error = null;
  let isLoading = false;

  onMount(async () => {
    await fetchImages();
  });


  const fetchImages = async () => {
    isLoading = true;
    error = null;
    try {
      const response = await axios.get(
        'http://localhost:8000/pictures/image_list/',
        { withCredentials: true }
      );
      images = response.data.images;
    } catch (err) {
      console.error('Error fetching images:', err);
      error = 'Failed to load images. Please try again.';
    } finally {
      isLoading = false;
    }
  };

  const getImageUrl = (image) => {
    // If the backend provides a full URL, use that
    if (image.url && image.url.startsWith('http')) {
      return image.url;
    }
    // Otherwise construct the URL pointing to the backend
    return `http://localhost:8000/${image.path}`;
  };
</script>

<div class="gallery">
  <h2>Image Gallery</h2>
  
  {#if isLoading}
    <div class="loading">Loading images...</div>
  {:else if error}
    <div class="error">{error}</div>
    <button on:click={fetchImages}>Retry</button>
  {:else if images.length === 0}
    <div class="empty">No images found</div>
  {:else}
    <div class="image-grid">
      {#each images as image (image.path)}
        <div class="image-item">
          <img 
            src={getImageUrl(image)} 
            alt={image.name}
            on:error={(e) => e.target.style.display = 'none'}
          />
          <div class="image-info">
            <p class="image-name">{image.name}</p>
            {#if image.uploaded_at}
              <p class="image-date">
                Uploaded: {new Date(image.uploaded_at).toLocaleDateString()}
              </p>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .gallery {
    margin: 20px;
    padding: 20px;
    font-family: Arial, sans-serif;
  }

  .loading, .error, .empty {
    text-align: center;
    padding: 20px;
    font-size: 1.2em;
  }

  .error {
    color: #d32f2f;
  }

  button {
    display: block;
    margin: 10px auto;
    padding: 8px 16px;
    background-color: #1976d2;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #1565c0;
  }

  .image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 25px;
    margin-top: 20px;
  }

  .image-item {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px;
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
  }

  .image-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
  }

  .image-item img {
    width: 100%;
    height: 200px;
    object-fit: contain;
    background: #f5f5f5;
    border-radius: 4px;
  }

  .image-info {
    padding: 10px 5px 5px;
  }

  .image-name {
    margin: 5px 0;
    font-weight: 500;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .image-date {
    margin: 0;
    font-size: 0.75em;
    color: #666;
  }
</style>