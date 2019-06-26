from datetime import datetime
from time import sleep
from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article
from unittest import skip

@skip('Skip Class')
class ArticlesViewTest(TestCase):
    """тест представления статей , раздел сайта 'Статьи'
    (kiteup.ru/articles/)"""

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

    def articles_objects_creation(self, n=1):
        """Создатель статей"""
        admin = User.objects.create_user(
            username='admin',
            password='123')

        for i in range(1, n+1):
            Article.objects.create(
                title=f'Название статьи {i}',
                published = date.today(),
                slug = f'slug-{i}',
                author=admin
                )

    def test_uses_all_articles_template(self):
        """тест: раздел Статьи (kiteup.ru/articles/)
         использует шаблон all_article.html"""
        response = self.client.get('/articles/')
        self.assertTemplateUsed(response, 'all_articles.html')

    def test_display_all_last_articles_on_articles_page(self):
        """тест: в разделе Статьи отображать все статьи"""
        self.articles_objects_creation(3)
        all_articles = Article.objects.all()
        self.assertGreater(len(all_articles), 1)


class ArticleViewTest(TestCase):
    """тест представления статьи , раздел сайта 'Статьи/Статья'
    (kiteup.ru/articles/slug)"""

    def articles_objects_creation(self, n=1):
        """Создатель статей"""
        admin = User.objects.create_user(
            username='admin',
            password='123')

        for i in range(1, n+1):
            Article.objects.create(
                title=f'Название статьи {i}',
                published = date.today(),
                slug = f'slug-{i}',
                author=admin,
                content=f'Текст статьи {i}'
                )

    def test_uses_all_articles_template(self):
        """тест: раздел Статьи/Сатья (kiteup.ru/articles/slug)использует
        шаблон article.html"""
        self.articles_objects_creation()
        response = self.client.get('/articles/slug-1')
        self.assertTemplateUsed(response, 'article.html')

    def test_display_article_title(self):
        """тест: у статьи есть заголовок"""
        self.articles_objects_creation()
        response = self.client.get('/articles/slug-1')
        self.assertContains(response, 'Название статьи 1')

    def test_display_article_author(self):
        """тест: у статьи есть автор"""
        self.articles_objects_creation()
        response = self.client.get('/articles/slug-1')
        self.assertContains(response, 'admin')


    def test_display_article_date_publication(self):
        """тест: у статьи есть дата публикации"""
        date_now = datetime.now().date()
        self.articles_objects_creation()
        response = self.client.get('/articles/slug-1')
        self.assertContains(response, date_now.strftime('%B %d, %Y'))

    def test_dysplay_article_content(self):
        """тест: собвстенно текст статьи"""
        self.articles_objects_creation()
        response = self.client.get('/articles/slug-1')
        self.assertContains(response,'Текст статьи 1')


# 1)Использовать тестовый клиент Django,
# 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
# 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
# 4) Проверить, чтобы все формы имели правильный класс.
# 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
# 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
# 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются