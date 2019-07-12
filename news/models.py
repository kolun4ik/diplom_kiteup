from django.db import models
from tinymce import HTMLField
from sorl.thumbnail import ImageField


class New(models.Model):
    """отдельная новость"""
    title = models.CharField(default='',max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(blank=True, null=True, max_length=250)
    content= HTMLField('Текст')
    image = ImageField(upload_to='news/',blank=True)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title