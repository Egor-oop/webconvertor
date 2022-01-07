from django.shortcuts import render, redirect
from django.views.generic import ListView

from .form import AudioFileForm
from .models import Audio

import os
from pydub import AudioSegment


def audio_convert(filename):
    os.chdir('media/audio')
    src = f'{filename}'
    dst = f'{filename}.wav'

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format='wav')
    os.chdir('../..')


def update_last(file_name):
    os.chdir('media/audio')
    A = Audio.objects.latest('id')
    file = A.id
    A.audio_file = f'audio/{file}.wav'
    print(file)
    old_name = f'{file_name}'
    new_name = f'{A.id}.wav'

    os.rename(old_name, new_name)
    A.save()
    os.chdir('../..')


def index(request):
    context = {'title': 'Home'}
    return render(request, 'mainapp/index.html', context)


def audio(request):
    context = {'title': 'Audio Upload'}

    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('audio_file').name
            form.save()
            audio_convert(file)
            update_last(file)
            return redirect('audio_converted')
    else:
        form = AudioFileForm()
    context['form'] = form
    return render(request, 'mainapp/audio.html', context)


class AudioDownloadListView(ListView):
    model = Audio
    template_name = 'mainapp/audio_download.html'

    def get_queryset(self, *, object_list=None, **kwargs):
        return super(AudioDownloadListView, self).get_queryset(**kwargs).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AudioDownloadListView, self).get_context_data(**kwargs)
        context['title'] = 'Download audio'
        return context


def error(request):
    return render(request, 'mainapp/error.html')
