from django.shortcuts import render


def index(request):
    context = {'title': 'Home'}
    return render(request, 'mainapp/index.html', context)

def audio(request):
    context = {'title': 'Audio'}
    return render(request, 'mainapp/audio.html', context)
