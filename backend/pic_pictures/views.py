from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'hotel_image_form.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded!')
