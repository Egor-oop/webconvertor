from django.db import models


class Audio(models.Model):
	audio_file = models.FileField(upload_to='audio/')
	format_ = (
		('.mp3', 'MP3'),
		('.wav', 'WAV'),
		('.ogg', 'OGG'),
	)
	convert_to = models.CharField(max_length=6, choices=format_, default='.wav')
