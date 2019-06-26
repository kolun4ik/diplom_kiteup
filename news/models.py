import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class ItemNews(models.Model):
    """отдельная новость"""
    title_news = models.CharField(default='',max_length=70)
    creation_date = models.DateTimeField(auto_now_add=True)
    content= models.TextField(default='')
    image = models.ImageField(upload_to='news/',blank=True)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title_news