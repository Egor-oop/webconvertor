from django.urls import path
from mainapp.views import index, audio, AudioDownloadListView, error

urlpatterns = [
    path('', index, name='index'),
    path('error', error, name='error'),
    path('audio/', audio, name='audio'),
    path('audio/download/', AudioDownloadListView.as_view(), name='audio_converted'),
]
