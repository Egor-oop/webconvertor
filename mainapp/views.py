from django.shortcuts import render, redirect
from django.views.generic import ListView

from .form import AudioFileForm
from .models import Audio

import os
from pydub import AudioSegment

os.chdir('media/audio')


def audio_convert(filename):
    src = f'{filename}'
    dst = f'{filename}.wav'

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format='wav')


def update_last():
    A = Audio.objects.latest('id')
    file = A.audio_file
    A.audio_file = f'{file}.wav'
    print(file)
    A.save()


def index(request):
    context = {'title': 'Home'}
    return render(request, 'mainapp/index.html', context)


def audio(request):
    context = {'title': 'Audio'}

    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('audio_file').name
            form.save()
            audio_convert(file)
            update_last()
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
