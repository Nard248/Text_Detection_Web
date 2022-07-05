from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from .models import Image
from .script import search_for_text
from Web_vision_Django.settings import MEDIA_ROOT


# Create your views here.

def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form['name'].value()
            return redirect(reverse("result",kwargs={'name':str(name)}))
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def success(request):
    return HttpResponse('Successfully Uploaded')


def process_view(request, name):
    image = Image.objects.get(name=name)
    path = search_for_text('WAITING', f'{MEDIA_ROOT}/{image.image}', name)
    return render(request, 'image_view.html', {'path': path})
