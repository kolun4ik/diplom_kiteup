from django.db import models

# Create your models here.

class Pages(models.Model):
    """Сраница основного раздела сайта kiteup.ru"""
    title = models.CharField(default='',max_length=80)
    body = models.TextField(default='')
