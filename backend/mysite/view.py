from django.http import HttpResponse
import os

MEDIA_ROOT =  os.path.join(os.getcwd(), 'media')

def upload_picture(request):
    return HttpResponse("Hello, world. You're at the polls index.")