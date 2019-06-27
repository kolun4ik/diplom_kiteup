import locale
import time
from .base import myTestCase
from articles.models import Article
from unittest import skip



# @skip('Skip Class')
class ArticlesViewTest(myTestCase):
    """тест представления статей , раздел сайта 'Статьи'
    (kiteup.ru/articles/)"""

    def test_uses_all_articles_template(self):
        """тест: раздел Статьи (kiteup.ru/articles/)
         использует шаблон all_article.html"""
        response = self.client.get('/articles/')
        self.assertTemplateUsed(response, 'all_articles.html')

    def test_display_all_last_articles_on_articles_page(self):
        """тест: в разделе Статьи отображать все статьи"""
        count = Article.objects.all().count()
        self.assertGreater(count, 1)


# @skip('Skip Class')
class ArticleViewTest(myTestCase):
    """тест представления статьи , раздел сайта 'Статьи/Статья'
    (kiteup.ru/articles/slug)"""

    def test_uses_all_articles_template(self):
        """тест: раздел Статьи/Сатья (kiteup.ru/articles/slug)использует
        шаблон article.html"""
        response = self.client.get('/articles/slug-1')
        self.assertTemplateUsed(response, 'article.html')

    def test_display_article_title(self):
        """тест: у статьи есть заголовок"""
        response = self.client.get('/articles/slug-1')
        self.assertContains(response, 'Название статьи 1')

    def test_display_article_author(self):
        """тест: у статьи есть автор"""
        response = self.client.get('/articles/slug-1')
        self.assertContains(response, 'admin')

    @skip('skip error locale output for cyr month')
    def test_display_article_date_publication(self):
        """тест: у статьи есть дата публикации"""
        locale.setlocale(locale.LC_ALL, 'Russian')
        date_now = time.strftime('%d %B, %Y', time.localtime())
        response = self.client.get('/articles/slug-1')
        self.assertContains(response, date_now)

    def test_dysplay_article_content(self):
        """тест: собвстенно текст статьи"""
        response = self.client.get('/articles/slug-1')
        self.assertContains(response,'Текст статьи 1')


# 1)Использовать тестовый клиент Django,
# 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
# 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
# 4) Проверить, чтобы все формы имели правильный класс.
# 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
# 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
# 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются