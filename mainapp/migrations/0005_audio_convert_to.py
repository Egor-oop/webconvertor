# Generated by Django 3.2.7 on 2022-01-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='convert_to',
            field=models.CharField(choices=[('.mp3', 'MP3'), ('.wav', 'WAV'), ('.ogg', 'OGG')], default='.wav', max_length=6),
        ),
    ]