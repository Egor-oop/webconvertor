from django.urls import path
from mainapp.views import index, audio

urlpatterns = [
    path('', index, name='index'),
    path('audio', audio, name='audio'),
    # path('convert_audio/<int:pk>', audio, name='audio_converted'),
]
