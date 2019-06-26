from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models import DO_NOTHING, CASCADE
from datetime import date


class Article(models.Model):
    """Отдельная статья"""
    slug = models.SlugField(default='',unique=True)
    title = models.CharField(default='', max_length=70)
    description = models.TextField('Описание', default='')
    content = models.TextField(default='')
    date_creation = models.DateTimeField(auto_now_add=True)
    published = models.DateField('опубликовано',null=True, blank=True,default=timezone.now)
    image = models.ImageField(upload_to='articles/', blank=True)
    author = models.ForeignKey(User, verbose_name='Автор',null=True,blank=True,on_delete=CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])