from django.db import models
from django.conf import settings
import os

class Image(models.Model):
    name = models.CharField(max_length=100)  # Add this
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
def get_images_from_directory(directory='uploads/'):
    """
    Get all image files from a specific directory in MEDIA_ROOT.
    Returns a list of Image model instances (both from DB and filesystem).
    For files not in DB, creates unsaved instances.
    """
    # Ensure directory path is properly normalized
    directory = directory.rstrip('/') # Ensure single trailing slash
    
    # Get absolute path to the directory
    abs_directory = os.path.join(os.getcwd(), directory)
    
    # Get all files from the directory
    try:
        all_files = os.listdir(abs_directory)
    except FileNotFoundError:
        return []
    
    # Filter image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']
    image_files = [
        f for f in all_files 
        if os.path.splitext(f)[1].lower() in image_extensions
    ]
    print(image_files)
    images_data = []
    for img_file in image_files:
        # Relative path (as it would be stored in the database)
        image_path = f"/{os.path.join(directory, img_file)}"
        
        # Check if image exists in database
        try:
            img_instance = Image.objects.get(image=image_path)
        except Image.DoesNotExist:
            # Create a new unsaved Image instance
            img_instance = Image(
                name=os.path.splitext(img_file)[0],  # Use filename without extension as name
                image=f"/{os.path.join(directory, img_file)}"
            )
        except Exception:
            print("Exception on finding image")
            
            
        images_data.append(img_instance)
    
    return images_data
