from django.forms import ModelForm

from .models import Video, Channel


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = {'title', 'channel', 'genre', 'clip', 'image_poster'}


class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = {'channel_name', 'channel_description', 'article_image'}

