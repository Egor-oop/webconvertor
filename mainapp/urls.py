from django.urls import path
from mainapp.views import index, audio, error

urlpatterns = [
    path('', index, name='index'),
    path('error', error, name='error'),
    path('audio/', audio, name='audio'),
]
