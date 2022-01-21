from django import forms

from .models import Video


class VideoFileForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_file', 'convert_to']
