from django.db import models
from django.utils import timezone
from tinymce import HTMLField


class Event(models.Model):
    """Объект: Мероприятие"""
    title = models.CharField(default='', max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateField('опубликовано', null=True, blank=True, default=timezone.now)
    content = HTMLField('Content')
    image = models.ImageField(upload_to='events/', blank=True)
    slug = models.SlugField(default='', unique=True)
    description = models.TextField('Описание', default='')
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('-published',)
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title