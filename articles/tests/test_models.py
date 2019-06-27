import os
import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from .base import myTestCase
from articles.models import Article




class ArticleModelTest(myTestCase):
    """тест модели Статья"""

    def test_can_save_a_article(self):
        """тест: можно сохранить статью в БД"""
        count = Article.objects.count()
        Article.objects.create(title='Следущая статья')
        self.assertEqual(Article.objects.count(), count + 1)

    def test_article_have_date_creation(self):
        """тест: статья имеет дату создания"""
        article = Article.objects.first()
        self.assertIsInstance(article.date_creation, datetime.datetime)

    def test_article_have_date_publication(self):
        """тест: статья имеет дату публикации"""
        article = Article.objects.first()
        self.assertEqual(article.published, timezone.now().date())

    def test_article_have_content(self):
        """тест: контент статьи"""
        article = Article.objects.first()
        self.assertEqual(article.content, 'Текст статьи 1')

    def test_article_have_image(self):
        """тест: каждая статья с картинкой"""
        article = Article.objects.first()
        self.assertIn( 'test_article.jpg', os.path.join(settings.STATIC_ROOT, str(article.image)))
        
    def test_article_have_unique_slug_url(self):
        """тест: статья имет уникадьный Url"""
        article1 = Article.objects.first()
        article2 = Article.objects.all()[1]
        self.assertNotEqual(article1.slug, article2.slug)

    def test_article_have_description(self):
        """тест: статья имеет краткое описание длинной 100 символов"""
        article = Article.objects.first()
        self.assertEqual(article.description, 'Краткое описание статьи длинной 100 знаков')

    def test_article_have_author(self):
        """тест: у статьи есть автор"""
        article = Article.objects.first()
        self.assertIsInstance(article.author, User)

