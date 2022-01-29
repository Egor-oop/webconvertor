from django import forms


class VideoFileForm(forms.Form):
    video_file = forms.FileField()
    convert_to = forms.CharField(max_length=6)
