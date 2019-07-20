import os
import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from .base import myTestCase
from articles.models import Article


class ArticleModelTest(myTestCase):
    """тест модели Статья"""

    def first(self):
        """Return first article object"""
        first = Article.objects.first()
        return first

    def test_can_save_a_article(self):
        """тест: можно сохранить статью в БД"""
        count = Article.objects.count()
        Article.objects.create(title='Следущая статья')
        self.assertNotEqual(Article.objects.count(), count)

    def test_article_have_date_created(self):
        """тест: статья имеет дату создания"""
        self.assertIsInstance(self.first().created, datetime.datetime)

    def test_article_have_date_publication(self):
        """тест: статья имеет дату публикации"""
        self.assertIsInstance(self.first().published, datetime.date)

    def test_article_have_date_updated(self):
        """тест: статья имеет дату создания"""
        self.assertIsInstance(self.first().updated, datetime.datetime)

    def test_article_have_content(self):
        """тест: контент статьи"""
        self.assertEqual(self.first().content, 'Текст статьи 3')

    def test_article_have_image(self):
        """тест: каждая статья с картинкой"""
        self.assertIn( 'test_article.jpg', os.path.join(settings.STATIC_ROOT, str(self.first().image)))
        
    def test_article_have_unique_slug_url(self):
        """тест: статья имет уникадьный Url"""
        article1 = Article.objects.all()[0]
        article2 = Article.objects.all()[1]
        self.assertNotEqual(article1.slug, article2.slug)

    def test_article_have_description(self):
        """тест: статья имеет краткое описание длинной 100 символов"""
        first = Article.objects.last()
        self.assertEqual(self.first().description, 'Краткое описание статьи 3')

    def test_article_have_author(self):
        """тест: у статьи есть автор"""
        article = Article.objects.first()
        self.assertIsInstance(article.author, User)

