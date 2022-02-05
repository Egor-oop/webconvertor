from django.shortcuts import render

import os
from django.core.files.storage import FileSystemStorage
import ffmpeg


def convert_video(filename, extension):
    os.chdir('media/video')
    full_name = None

    if extension == '.mov':
        stream = ffmpeg.input(f'{filename}')
        stream = ffmpeg.output(stream, f'{filename[:-4]}.mov')
        full_name = f'{filename[:-4]}.mov'
        try:
            ffmpeg.run(stream)
        except:
            os.chdir('../..')
            return 'Unknown extension'

    elif extension == '.avi':
        stream = ffmpeg.input(f'{filename}')
        stream = ffmpeg.output(stream, f'{filename[:-4]}.avi')
        full_name = f'{filename[:-4]}.avi'
        try:
            ffmpeg.run(stream)
        except:
            os.chdir('../..')
            return 'Unknown extension'
    elif extension == '.mp4':
        stream = ffmpeg.input(f'{filename}')
        stream = ffmpeg.output(stream, f'{filename[:-4]}.mp4')
        full_name = f'{filename[:-4]}.mp4'
        try:
            ffmpeg.run(stream)
        except:
            os.chdir('../..')
            return 'Unknown extension'
    os.remove(filename)
    os.chdir('../..')
    return full_name


def index(request):
    try:
        if request.method == 'POST' and request.FILES['upload'] and request.POST:
            upload = request.FILES['upload']
            fss = FileSystemStorage(location='media/video/')
            file = fss.save(upload.name, upload)
            extension = request.POST.get('convert_to')
            full_name = convert_video(file, extension)
            if full_name == 'Unknown extension':
                fss = FileSystemStorage(location='../../')
                return render(request, 'videoapp/video.html', {'extension_error': full_name, 'title': 'Video Upload'})
            file_url = fss.url(f'/video/{full_name}')
            return render(request, 'videoapp/video.html', {'file_url': file_url, 'title': 'Video Upload'})
    except:
        return render(request, 'videoapp/video.html', {'load_error': 'Please load a file', 'title': 'Video Upload'})
    return render(request, 'videoapp/video.html', {'title': 'Video Upload'})
