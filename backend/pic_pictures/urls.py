from django.urls import path

from . import views

urlpatterns = [
    path('image_upload/', views.image_upload, name='image_upload'),
    path('image_list/', views.image_list, name='image_list'),
    path('image_download/', views.image_download, name='image_download'),
    path('success/', views.success, name='success')
]
