from django import forms

from .models import Audio


class AudioFileForm(forms.ModelForm):
	class Meta:
		model = Audio
		fields = ['audio_file', 'convert_to']
