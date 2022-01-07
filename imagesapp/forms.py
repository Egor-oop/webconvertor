from django import forms

from .models import Image


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_file']
