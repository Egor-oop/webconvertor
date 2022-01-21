from django.urls import path
from videoapp.views import index, VideoDownloadListView

urlpatterns = [
    path('', index, name='video'),
    path('download/', VideoDownloadListView.as_view(), name='video_converted'),
]