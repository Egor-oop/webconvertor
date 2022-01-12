from django.db import models


class Image(models.Model):
    image_file = models.FileField(upload_to='images/')
    format_ = (
        ('.jpg', 'JPG'),
        ('.png', 'PNG'),
        ('.jfif', 'JFIF'),
    )
    convert_to = models.CharField(max_length=6, choices=format_, default='.png')
