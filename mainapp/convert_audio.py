import os
from pydub import AudioSegment

os.chdir('media/audio')


def audio_convert(filename):
    src = f'{filename}'
    dst = f'{filename}.wav'

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format='wav')
