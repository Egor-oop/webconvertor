from django.urls import path
from imagesapp.views import index

urlpatterns = [
    path('', index, name='images'),
]
