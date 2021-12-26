from django.db import models


class Audio(models.Model):
	audio_file = models.FileField(upload_to='audio/')
