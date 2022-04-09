from django.db import models
from django.core.validators import FileExtensionValidator


class Channel(models.Model):
    """Класс модели Channel"""
    channel_name = models.CharField(max_length=50,
                                    verbose_name='Название канала')
    channel_description = models.TextField(verbose_name='Описание канала')
    article_image = models.ImageField(null=True, blank=True,
                                       upload_to='image/',
                                       verbose_name='Изображение')

    class Meta:
        verbose_name = 'Видеоканал'
        verbose_name_plural = 'Видеоканалы'
        ordering = ['channel_name']

    def __str__(self):
        """Вызывает название канала"""
        return self.channel_name


class Genre(models.Model):
    """Класс модели Genre"""
    genre_name = models.CharField(max_length=30, verbose_name='Жанр видео')

    class Meta:
        verbose_name = 'Жанр видео'
        verbose_name_plural = 'Жанр видео'

    def __str__(self):
        """Вызывает название видео"""
        return self.genre_name


class Video(models.Model):
    """Класс модели Video"""
    title = models.CharField(max_length=150, verbose_name='Заголовок видео')
    channel = models.ForeignKey('Channel', on_delete=models.PROTECT,
                                verbose_name='Название канала')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT,
                                verbose_name='Название жанра видео')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Дата публикации')
    clip = models.FileField(upload_to='video/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=['mp4'])],
                            verbose_name='Видеоролик')
    image_poster = models.FileField(upload_to='image/',
                                    verbose_name='Превью видео')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['-published']

