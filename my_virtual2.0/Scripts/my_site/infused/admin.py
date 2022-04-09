from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Channel, Video, Genre


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'published', 'clip', 'genre',
                    'get_poster')
    list_display_links = ('title', 'channel')
    search_fields = ('title', 'channel')

    def get_poster(self, img):
        return mark_safe(f'<img src={img.image_poster.url} width="120"'
                         f' height="60"')

    get_poster.short_description = "Превью видео"


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.article_image.url} width="70" '
                          f'height="70"')

    get_image.short_description = "Изображение"


admin.site.register(Video, VideoAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Genre)
admin.site.site_title = "Django Infused"
admin.site.site_header = "Django Infused"
