from django.db import models

# Create your models here.
class ItemNews(models.Model):
    """отдельная новость"""
    text = models.TextField(default='')