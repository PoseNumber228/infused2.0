from django.urls import path, re_path
from .views import add_video, add_channel
from django.conf import settings

from . import views

app_name = 'infused'
urlpatterns = [
    path('', views.index, name='index'),
    path('channel/<int:channel_id>/', views.get_channel, name='get_channel'),
    path('genre/<int:genre_id>/', views.genre_filter, name='genre_filter'),
    path('add_videos/', views.add_video, name='add_videos'),
    path('add_channels/', views.add_channel, name='add_channels'),
    path('search_list/', views.search_channel, name='search'),
]
