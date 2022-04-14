from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db.models import Q

from .forms import VideoForm, ChannelForm

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
    descriptions = Channel.objects.get(pk=channel_id)
    current_channel = Channel.objects.get(pk=channel_id)
    videos = Video.objects.filter(channel=channel_id)
    channels = Channel.objects.all()
    context = {
        'images': images,
        'descriptions': descriptions,
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
        video_form = VideoForm()
    else:
        video_form = VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            add_videos = video_form.save(commit=False)
            add_videos.save()
            return redirect('infused:index')

    context = {
        'video_form': video_form
    }
    return render(request, 'infused/add_video.html', context)


def add_channel(request):
    """Позволяет польователю создать канал."""
    if request.method != 'POST':
        channel_form = ChannelForm()
    else:
        channel_form = ChannelForm(request.POST, request.FILES)
        if channel_form.is_valid():
            create_channels = channel_form.save(commit=False)
            create_channels.save()
            return redirect('infused:index')

    context = {
        'channel_form': channel_form
    }
    return render(request, 'infused/add_channel.html', context)


def search_channel(request):
    """Поиск"""
    if request.method == "POST":
        searched = request.POST['searched']
        values = Video.objects.filter(
            title__iregex=searched
        )
        context = {
            'searched': searched,
            'values': values,
        }
        return render(request, 'infused/search_list.html', context)
    else:
        return render(request, 'infused/search_list.html', {})


