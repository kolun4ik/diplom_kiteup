from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.shortcuts import reverse
from tinymce import HTMLField
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User



class Article(models.Model):
    """Статья"""
    slug = models.SlugField(default='',unique=True)
    title = models.CharField(default='', max_length=70)
    description = models.TextField('Описание', default='')
    content = HTMLField('Content')
    date_creation = models.DateTimeField(auto_now_add=True)
    published = models.DateField('опубликовано',null=True, blank=True,default=timezone.now)
    image = ImageField(upload_to='articles/', blank=True)
    author = models.ForeignKey(User, verbose_name='Автор',null=True,blank=True,on_delete=CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published',)
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])