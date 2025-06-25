from django.urls import path

from . import views

urlpatterns = [
    path('image_upload/', views.image_upload, name='image_upload'),
    path('image_download/', views.image_download, name='image_download'),
    path('success/', views.success, name='success')
]
