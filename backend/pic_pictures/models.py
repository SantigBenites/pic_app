from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)  # Add this
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name