from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from tinymce import HTMLField
from sorl.thumbnail import ImageField


class Event(models.Model):
    """Объект: Мероприятие"""
    slug = models.SlugField('Url', default='', unique=True)
    title = models.CharField('Заголовок', default='', max_length=80)
    longtitle = models.CharField('Заголовок страницы', default='', max_length=150)
    created = models.DateTimeField('Создан', auto_now_add=True)
    published = models.DateField('Опубликовано', null=True, blank=True, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField('Описание (SEO)', default='', max_length=120)
    introtext = models.CharField('Введение', default='', max_length=300)
    content = HTMLField('Содержимое')
    image = ImageField('Превью', upload_to='events/', blank=True)
    visible = models.BooleanField('Опубликован', default=True)

    class Meta:
        ordering = ('-published',)
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        db_table = 'events'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', args=[str(self.slug)])