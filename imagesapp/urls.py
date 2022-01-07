from django.urls import path
from imagesapp.views import index, ImageDownloadListView

urlpatterns = [
    path('', index, name='images'),
    path('download/', ImageDownloadListView.as_view(), name='image_converted'),
]
