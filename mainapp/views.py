from django.shortcuts import render

import os
from django.conf import settings
from django.http import HttpResponse, Http404

from django.core.files.storage import FileSystemStorage
from pydub import AudioSegment


def audio_convert(filename, extension):
    os.chdir('media/audio')
    full_name = None

    if extension == '.wav':
        src = f'{filename}'
        dst = f'{filename[:-4]}.wav'

        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format='wav')

        full_name = f'{filename[:-4]}.wav'
    elif extension == '.mp3':
        src = f'{filename}'
        dst = f'{filename[:-4]}.mp3'

        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format='mp3')

        full_name = f'{filename[:-4]}.mp3'
    elif extension == '.ogg':
        src = f'{filename}'
        dst = f'{filename[:-4]}.ogg'

        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format='ogg')

        full_name = f'{filename[:-4]}.wav'

    os.remove(filename)
    os.chdir('../..')
    return full_name


def index(request):
    context = {'title': 'Home'}
    return render(request, 'mainapp/index.html', context)


def audio(request):
    if request.method == 'POST' and request.FILES['upload'] and request.POST:
        upload = request.FILES['upload']
        fss = FileSystemStorage(location='media/audio/')
        file = fss.save(upload.name, upload)
        extension = request.POST.get('convert_to')
        full_name = audio_convert(file, extension)
        file_url = fss.url(f'/audio/{full_name}')
        return render(request, 'mainapp/audio.html', {'file_url': file_url, 'title': 'Audio Upload'})
    return render(request, 'mainapp/audio.html', {'title': 'Audio Upload'})


# def download(request, filename):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)


def error(request):
    return render(request, 'mainapp/error.html')
