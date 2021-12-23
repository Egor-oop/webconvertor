from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pydub import AudioSegment
import os


os.chdir('media')


def audio_convert(filename):
    src = f'{filename}'
    dst = f'{filename}.wav'

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format='wav')


def index(request):
    context = {'title': 'Home'}
    return render(request, 'mainapp/index.html', context)


def audio(request):
    context = {'title': 'Audio'}

    if request.method == 'POST':
        uploaded_file = request.FILES['audio']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        audio_convert(uploaded_file.name)

        return HttpResponseRedirect('/')

    # context['form'] = form
    return render(request, 'mainapp/audio.html', context)
