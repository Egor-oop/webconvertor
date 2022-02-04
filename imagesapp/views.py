from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage

from PIL import Image as PImage

import os


def convert_image(filename, extension):
    rgb_im = None
    full_name = None
    os.chdir('media/images')

    try:
        image = PImage.open(f'{filename}')
        rgb_im = image.convert('RGB')
    except IOError:
        redirect('error')

    if extension == '.png':
        try:
            rgb_im.save(filename[:-4] + '.png')
        except AttributeError:
            os.chdir('../..')
            return 'Unknown extension'
        full_name = f'{filename[:-4]}.png'
    elif extension == '.jpg':
        try:
            rgb_im.save(filename[:-4] + '.jpg')
        except AttributeError:
            os.chdir('../..')
            return 'Unknown extension'
        full_name = f'{filename[:-4]}.jpg'
    elif extension == '.jfif':
        try:
            rgb_im.save(filename[:-4] + '.jfif')
        except AttributeError:
            os.chdir('../..')
            return 'Unknown extension'
        full_name = f'{filename[:-4]}.jfif'

    os.remove(filename)
    os.chdir('../..')
    return full_name


def index(request):
    if request.method == 'POST' and request.FILES['upload'] and request.POST:
        upload = request.FILES['upload']
        fss = FileSystemStorage(location='media/images/')
        file = fss.save(upload.name, upload)
        extension = request.POST.get('convert_to')
        full_name = convert_image(file, extension)
        if full_name == 'Unknown extension':
            fss = FileSystemStorage(location='../../')
            return render(request, 'imagesapp/image.html', {'extension_error': full_name, 'title': 'Image Upload'})
        file_url = fss.url(f'/images/{full_name}')
        return render(request, 'imagesapp/image.html', {'file_url': file_url, 'title': 'Image Upload'})
    return render(request, 'imagesapp/image.html', {'title': 'Image Upload'})
