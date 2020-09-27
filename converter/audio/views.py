

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from os import path
import subprocess
import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        audio_fpath = os.path.abspath(os.path.join('media\\' + uploaded_file.name))
        output = audio_fpath[:-4] + ".wav"
        subprocess.call(['ffmpeg', '-i', audio_fpath, output])
        x, sr = librosa.load(output)
        plt.figure(figsize=(14, 5))
        librosa.display.waveplot(x, sr=sr, color='gray')
        plt.savefig(audio_fpath[:-4] + ".png")
        context['plot'] = (('\\media\\' + uploaded_file.name)[:-4] + ".png")

    return render(request, 'upload.html', context)
