from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ImageForm
from django.views.decorators.csrf import ensure_csrf_cookie
import os


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

    # specify the img directory path
    path = "path/to/img/folder/"

    # list files in img directory
    files = os.listdir(path)

    for file in files:
        # make sure file is an image
        if file.endswith(('.jpg', '.png', 'jpeg')):
            img_path = path + file
    return

def image_download(request):
    if request.method == 'GET':
        request
        try:
            with open(valid_image, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
    return JsonResponse({'message': 'GET requests only'}, status=405)

def success(request):
    return HttpResponse('Successfully uploaded!')
