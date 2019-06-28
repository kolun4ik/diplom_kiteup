from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article


class myTestCase(TestCase):
    """TestCase extended method"""

    @classmethod
    def setUpTestData(cls):
        """Создадим несколько статей"""
        admin = User.objects.create_user(
            username='admin',
            password='123')

        for i in range(1, 4):
            Article.objects.create(
                title=f'Название статьи {i}',
                published=date.today(),
                slug=f'slug-{i}',
                author=admin,
                description = 'Краткое описание статьи длинной 100 знаков',
                content=f'Текст статьи {i}',
                image='/articles/test_article.jpg',
            )