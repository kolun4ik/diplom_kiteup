from django.db import models
from django.urls import reverse

# Create your models here.
class ItemNews(models.Model):
    """отдельная новость"""
    text = models.TextField(default='')

    # #Заготовка "разрешения" URL
    # def get_absolute_url(self):
    #     """Получить абсолютный URL"""
    #     return reverse('news_view', args=[self.id])