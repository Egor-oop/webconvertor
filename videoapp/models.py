from django.db import models


class Video(models.Model):
	video_file = models.FileField(upload_to='video/')
	format_ = (
		('.mp4', 'MP4'),
		('.avi', 'AVI'),
		('.mov', 'MOV'),
	)
	convert_to = models.CharField(max_length=6, choices=format_, default='.mp4')