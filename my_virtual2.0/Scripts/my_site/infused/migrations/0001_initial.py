# Generated by Django 3.2.9 on 2022-04-12 09:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=50, verbose_name='Название канала')),
                ('channel_description', models.TextField(verbose_name='Описание канала')),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Видеоканал',
                'verbose_name_plural': 'Видеоканалы',
                'ordering': ['channel_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=30, verbose_name='Жанр видео')),
            ],
            options={
                'verbose_name': 'Жанр видео',
                'verbose_name_plural': 'Жанр видео',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок видео')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('clip', models.FileField(upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Видеоролик')),
                ('image_poster', models.FileField(blank=True, upload_to='image/', verbose_name='Превью видео(Не обязательно)')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='infused.channel', verbose_name='Название канала')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='infused.genre', verbose_name='Название жанра видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'ordering': ['-published'],
            },
        ),
    ]
