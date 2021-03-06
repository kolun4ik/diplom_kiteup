# Generated by Django 2.1.9 on 2019-08-08 12:01

from django.db import migrations, models
import django.utils.timezone
import sorl.thumbnail.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', unique=True, verbose_name='Url')),
                ('title', models.CharField(default='', max_length=70, verbose_name='Заголовок')),
                ('longtitle', models.CharField(default='', max_length=150, verbose_name='Заголовок страницы')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('published', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Опубликовано')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(default='', max_length=120, verbose_name='Описание (SEO)')),
                ('introtext', models.CharField(default='', max_length=300, verbose_name='Введение')),
                ('content', tinymce.models.HTMLField(verbose_name='Содержимое')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='news/')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='published', max_length=12)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
            },
        ),
    ]
