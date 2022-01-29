from django.urls import path
from videoapp.views import index

urlpatterns = [
    path('', index, name='video'),
]