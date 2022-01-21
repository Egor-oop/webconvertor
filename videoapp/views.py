from django.shortcuts import render, redirect
from django.views.generic import ListView

from .form import VideoFileForm
from .models import Video

import os
from django.shortcuts import render
import ffmpeg

#stream = ffmpeg.input('video_1.mp4')
#stream = ffmpeg.output(stream, 'o12.MOV')
#ffmpeg.run(stream)


def convert_video(filename):
    os.chdir('media/video')
    A = Video.objects.latest('id')
    file = A.id
    print(file)

    stream = ffmpeg.input(f'video/{file}')
    stream = ffmpeg.output(stream, 'new_filename.MOV')
    ffmpeg.run(stream)


    # A.convert_to == '.png':
    # A.image_file = f'images/{file}.png'
    # rgb_im.save(filename + '.png')
    # old_name = f'{filename}'
    # new_name = f'{A.id}.png'
    # os.rename(old_name, new_name)
    # A.save()


class VideoDownloadListView(ListView):
    model = Video
    template_name = 'mainapp/video_download.html'

    def get_queryset(self, *, object_list=None, **kwargs):
        return super(VideoDownloadListView, self).get_queryset(**kwargs).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VideoDownloadListView, self).get_context_data(**kwargs)
        context['title'] = 'Download video'
        return context

def index(request):
    context = {'title': 'Video Upload'}

    if request.method == 'POST':
        form = VideoFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('video_file').name
            form.save()
            convert_video(file)
            return redirect('video_converted')
    else:
        form = VideoFileForm()
    context['form'] = form
    return render(request, 'videoapp/video.html', context)