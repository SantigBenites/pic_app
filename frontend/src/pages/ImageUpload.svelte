<script>
  import axios from 'axios';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let file = null;
  let uploadStatus = '';
  let csrfToken = '';

  onMount(async () => {
    await fetchCSRFToken();
  });

  const fetchCSRFToken = async () => {
    try {
      const response = await axios.get(
        'http://localhost:8000/csrf_token_endpoint/', 
        { withCredentials: true }
      );
      csrfToken = response.data.csrfToken;
    } catch (error) {
      console.error('Error fetching CSRF token:', error);
      uploadStatus = 'Error getting security token. Please refresh the page.';
    }
  };

  const handleFileChange = (e) => {
    file = e.target.files[0];
    uploadStatus = '';
  };

  const uploadImage = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('name', file.name);
    formData.append('image', file);

    try {
      const response = await axios.post(
        'http://localhost:8000/pictures/image_upload/', 
        formData, 
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': csrfToken
          },
          withCredentials: true
        }
      );
      
      uploadStatus = `Upload successful! File ID: ${response.data.id}`;
      file = null;
      // Navigate to gallery after successful upload
      setTimeout(() => goto('/gallery'), 1500);
    } catch (error) {
      if (error.response?.status === 403) {
        await fetchCSRFToken();
        uploadStatus = 'Security token expired. Try uploading again.';
      } else {
        uploadStatus = `Upload failed: ${error.response?.data?.message || error.message}`;
      }
    }
  };
</script>

<div class="upload-container">
  <h2>Upload Image</h2>
  <input type="file" accept="image/*" on:change={handleFileChange} />
  <button on:click={uploadImage} disabled={!file}>Upload</button>
  
  {#if uploadStatus}
    <p class:error={uploadStatus.includes('failed') || uploadStatus.includes('Error')}>
      {uploadStatus}
    </p>
  {/if}
</div>

<style>
  .upload-container {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    max-width: 500px;
    margin: 0 auto;
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
  .error {
    color: red;
  }
</style>