<script>
  export let images = [];
</script>

<div class="gallery">
  <h2>Image Gallery</h2>
  <div class="image-grid">
    {#each images as image}
      <div class="image-item">
        <img 
          src={`http://localhost:8000/api/image/${image}`} 
          alt={image}
          on:error={(e) => e.target.style.display = 'none'}
        />
        <p>{image}</p>
      </div>
    {/each}
  </div>
</div>

<style>
  .gallery {
    margin: 20px;
    padding: 20px;
  }
  .image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
  }
  .image-item {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
  }
  .image-item img {
    width: 100%;
    height: 200px;
    object-fit: contain;
  }
  .image-item p {
    text-align: center;
    margin: 5px 0;
    font-size: 0.8em;
    word-break: break-all;
  }
</style>