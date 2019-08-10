from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from tinymce import HTMLField
from sorl.thumbnail import ImageField


class New(models.Model):
    """Yовость"""

    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    slug = models.SlugField('Url', default='', unique=True)
    title = models.CharField('Заголовок',default='',max_length=70)
    longtitle = models.CharField('Заголовок страницы', default='', max_length=150)
    created = models.DateTimeField('Создан',auto_now_add=True)
    published = models.DateField('Опубликовано', null=True, blank=True, default=timezone.now)
    updated = models.DateTimeField('Обновлено', auto_now=True, null=True, blank=True)
    description = models.CharField('Описание (SEO)', default='', max_length=120)
    introtext = models.CharField('Введение', default='', max_length=300)
    content= HTMLField('Содержимое')
    image = ImageField(upload_to='news/',blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='published')


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = "news"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('club-news', args=[str(self.slug)])