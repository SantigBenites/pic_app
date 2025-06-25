from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ImageForm
from django.views.decorators.csrf import ensure_csrf_cookie


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

def image_get_all(request):
    return

def image_download(request):
    return HttpResponse('Successfully uploaded!')

def success(request):
    return HttpResponse('Successfully uploaded!')
