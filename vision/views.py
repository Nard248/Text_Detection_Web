from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .script import search_for_text
from .models import Image
import numpy as np
# Create your views here.
def index(request):
    return HttpResponse('This is index')


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def processed_view(request):
    image = Image.objects.get(name='Test')
    return render(request, "processed.html", {
        'path': search_for_text('TEXT', 'media\\' + str(image.Img), image.name + '.jpeg')
    })
