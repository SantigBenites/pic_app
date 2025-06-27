from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
import os

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(os.getcwd(), 'media')

urlpatterns = [
    path('image_upload/', views.image_upload, name='image_upload'),
    path('image_list/', views.image_list, name='image_list'),
    path('success/', views.success, name='success')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
