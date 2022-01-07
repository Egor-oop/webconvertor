from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import ImageFileForm
from .models import Image

from PIL import Image as PImage

import sys
import os


def convert_image(filename):
    try:
        image = PImage.open(f'{filename}')
    except IOError:
        redirect('error')

    rgb_im = image.convert('RGB')
    rgb_im.save(filename + '.wav')


def index(request):
    context = {'title': 'Image Upload'}

    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageFileForm()
    context['form'] = form
    return render(request, 'imagesapp/image.html', context)


class ImageDownloadListView(ListView):
    model = Image
    template_name = 'imagesapp/image_download.html'

    def get_queryset(self, *, object_list=None, **kwargs):
        return super(ImageDownloadListView, self).get_queryset(**kwargs).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ImageDownloadListView, self).get_context_data(**kwargs)
        context['title'] = 'Download image'
        return context
