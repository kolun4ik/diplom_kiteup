import datetime
import os
from django.test import TestCase
from articles.models import Article
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

USER_NAME = 'admin'
USER_EMAIL = '1@r.ru'
PASSWORD = '123'


class ArticleModelTest(TestCase):
    """тест модели Статья"""

    def test_saving_and_retriving_articles(self):
        """тест сохранения и получения отдельной взятой стаьи из
        таблицы статей"""
        first_article = Article()
        first_article.title = 'Статья 1'
        first_article.date_publication = datetime.date.today()
        first_article.slug = '1'
        first_article.save()

        second_article = Article()
        second_article.title = 'Статья 2'
        second_article.date_publication = datetime.date.today()
        second_article.slug = '2'
        second_article.save()

        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 2)

        first_saved_article = saved_articles[0]
        second_saved_article = saved_articles[1]

        self.assertEqual(first_saved_article.title, 'Статья 1')
        self.assertEqual(second_saved_article.title, 'Статья 2')

    def test_can_save_a_article(self):
        """тест: можно сохранить статью в БД"""
        self.assertEqual(Article.objects.count(),0)
        Article.objects.create(title='Статья 1')
        self.assertEqual(Article.objects.count(), 1)

    def test_article_have_date_creation(self):
        """тест: статья имеет дату создания"""
        article = Article.objects.create(title='Статья 1')
        self.assertIsInstance(article.date_creation, datetime.datetime)

    def test_article_have_date_publication(self):
        """тест: статья имеет дату публикации"""
        article = Article.objects.create(
            title='Статья 1',
            published=timezone.now().date())
        self.assertEqual(article.published, timezone.now().date())

    def test_article_have_content(self):
        """тест: контент статьи"""
        text_content = 'Lorem ipsum'
        article = Article.objects.create(
            title='Статья 1',
            published= datetime.date.today(),
            content=text_content)
        self.assertEqual(article.content, 'Lorem ipsum')

    def test_article_have_image(self):
        """тест: каждая статья с картинкой"""
        article = Article.objects.create(
            title='Статья 1',
            content='Lorem ipsum',
            image='/articles/test_article.jpg')
        self.assertIn( 'test_article.jpg', os.path.join(settings.STATIC_ROOT, str(article.image)))
        
    def test_article_have_unique_slug_url(self):
        """тест: статья имет уникадьный Url"""
        article1 = Article.objects.create(
            title='Статья 1',
            slug = '123')
        article2 = Article.objects.create(
            title='Статья 2',
            slug='345')
        self.assertNotEqual(article1.slug, article2.slug)

    def test_article_have_description(self):
        """тест: статья имеет короткое описание длиной 100 символов"""
        article = Article.objects.create(
            title='Статья 1',
            published=datetime.date.today(),
            description='О чем статья, кратко')
        self.assertEqual(article.description, 'О чем статья, кратко')

    def test_article_have_author(self):
        """тест: у статьи есть автор"""
        admin = User.objects.create_user(
            username=USER_NAME,
            password=PASSWORD)
        article = Article.objects.create(
            title='Статья 1',
            slug='123',
            author=admin)
        self.assertIsInstance(article.author, User)

