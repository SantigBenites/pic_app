<script>
  import axios from 'axios';
  import { onMount } from 'svelte';

  let file = null;
  let uploadStatus = '';
  let images = [];

  const handleFileChange = (e) => {
    file = e.target.files[0];
  };

  const uploadImage = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:8000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      uploadStatus = `Upload successful! File ID: ${response.data}`;
      file = null;
      fetchImages(); // Refresh the image list
    } catch (error) {
      uploadStatus = `Upload failed: ${error.message}`;
    }
  };

  const fetchImages = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/images');
      images = response.data;
    } catch (error) {
      console.error('Error fetching images:', error);
    }
  };

  onMount(() => {
    fetchImages();
  });
</script>

<div class="upload-container">
  <h2>Upload Image</h2>
  <input type="file" accept="image/*" on:change={handleFileChange} />
  <button on:click={uploadImage} disabled={!file}>Upload</button>
  {#if uploadStatus}
    <p>{uploadStatus}</p>
  {/if}
</div>

<style>
  .upload-container {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  button {
    margin-top: 10px;
    padding: 8px 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
</style>