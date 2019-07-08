import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class New(models.Model):
    """отдельная новость"""
    title = models.CharField(default='',max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(blank=True, null=True, max_length=250)
    content= models.TextField(default='')
    image = models.ImageField(upload_to='news/',blank=True)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title