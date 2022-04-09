from django.urls import path, re_path
from .views import add_video
from django.conf import settings

from . import views

app_name = 'infused'
urlpatterns = [
    path('', views.index, name='index'),
    path('c/<int:channel_id>/', views.get_channel, name='get_channel'),
    path('g/<int:genre_id>/', views.genre_filter, name='genre_filter'),
    path('add/', views.add_video, name='add'),
    path('', views.Search.as_view(), name='search'),
]
