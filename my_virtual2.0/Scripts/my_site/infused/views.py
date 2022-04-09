from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db.models import Q

from .forms import VideoForm

from .models import Video, Channel, Genre


def index(request):
    """Добавляет видео и жанры на главную страницу"""
    videos = Video.objects.all()
    titles = Video.objects.all()
    channels = Channel.objects.all()
    genres = Genre.objects.all()
    context = {
        'videos': videos,
        'titles': titles,
        'channels': channels,
        'genres': genres
    }
    return render(request, 'infused/index.html', context)


def get_channel(request, channel_id):
    """Выводит канал по его названию"""
    images = Channel.objects.get(pk=channel_id)
    videos = Video.objects.filter(channel=channel_id)
    channels = Channel.objects.all()
    current_channel = Channel.objects.get(pk=channel_id)
    context = {
        'images': images,
        'videos': videos,
        'channels': channels,
        'current_channel': current_channel
    }
    return render(request, 'infused/channel.html', context)


def genre_filter(request, genre_id):
    """Фильтрует все видео по жанрам"""
    videos = Video.objects.filter(genre=genre_id)
    genres = Genre.objects.all()
    current_genre = Genre.objects.get(pk=genre_id)
    context = {
        'videos': videos,
        'genres': genres,
        'current_genre': current_genre
    }
    return render(request, 'infused/genre_filter.html', context)



def add_video(request):
    """Добавляет видео на канал."""
    if request.method != 'POST':
        form = VideoForm()
    else:
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            add_video = form.save(commit=False)
            add_video.save()
            return redirect('infused:index')

    context = {
        'form': form
    }
    return render(request, 'infused/add_video.html', context)


class Search(ListView):
    """Поиск"""
    paginate_by = 4

    def get_queryset(self):
        return Video.objects.filter(
            title__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context

