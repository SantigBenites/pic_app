from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ImageForm
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Image, get_images_from_directory
import os
from django.conf import settings
import datetime 


@ensure_csrf_cookie
def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return JsonResponse({'id': instance.id, 'status': 'success'})
        # Return detailed form errors
        return JsonResponse({
            'status': 'error',
            'errors': dict(form.errors.items()),
            'fields': list(form.fields.keys())  # Show expected fields
        }, status=400)
    return JsonResponse({'message': 'POST requests only'}, status=405)



def image_list(request):
    try:
        # Get all images (both from DB and filesystem)
        image_instances = get_images_from_directory()

        images_data = []
        for img in image_instances:
            try:
                # For unsaved instances (from filesystem)
                if not img.pk:
                    # Create proper URL for filesystem images
                    relative_path = str(img.image).replace('\\', '/')
                    media_url = settings.MEDIA_URL.rstrip('/') + '/'
                    
                    img_data = {
                        'name': img.name,
                        'path': relative_path,
                        'url': f"{media_url}{relative_path}",
                        'uploaded_at': datetime.datetime.now().isoformat(),
                        'status': 'filesystem'
                    }
                else:
                    # For saved instances (from database)
                    img_data = {
                        'id': img.pk,
                        'name': img.name,
                        'url': img.image.url if img.image else None,
                        'path': str(img.image) if img.image else None,
                        'uploaded_at': img.uploaded_at.isoformat(),
                        'status': 'database'
                    }
                images_data.append(img_data)
            except Exception as e:
                print(f"Error processing image {getattr(img, 'name', 'unknown')}: {str(e)}")
                continue
        
        return JsonResponse({
            'status': 'success',
            'count': len(images_data),
            'data': images_data
        })
    
    except Exception as e:
        print(f"Server error: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': "Internal server error"
        }, status=500)

def success(request):
    return HttpResponse('Successfully uploaded!')
