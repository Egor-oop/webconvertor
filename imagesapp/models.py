from django.db import models


class Image(models.Model):
    image_file = models.FileField(upload_to='images/')
