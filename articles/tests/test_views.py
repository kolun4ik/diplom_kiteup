import locale
import time
from .base import myTestCase
from articles.models import Article
from articles.views import ArticlesListView, ArticleDetailView
from unittest import skip


# @skip('Skip Class')
class ArticlesViewTest(myTestCase):
    """тест представления статей , раздел сайта 'Статьи'
    (kiteup.ru/articles/)"""

    def setUp(self):
        """Начальные установки"""
        self.response = self.client.get('/articles/')

    def test_uses_all_articles_template(self):
        """тест: раздел Статьи (kiteup.ru/articles/)
         использует шаблон all_article.html"""
        self.assertTemplateUsed(self.response, 'articles/all_articles.html')

    def test_event_uses_view_as_class_based_view(self):
        """тест: использование представления Event как Class-Based view"""
        self.assertEqual(
            self.response.resolver_match.func.__name__,
            ArticlesListView.as_view().__name__)

    def test_display_all_last_articles_on_articles_page(self):
        """тест: в разделе Статьи отображать все статьи"""
        count = Article.objects.all().count()
        self.assertGreater(count, 1)


# @skip('Skip Class')
class ArticleViewTest(myTestCase):
    """тест представления статьи , раздел сайта 'Статьи/Статья'
    (kiteup.ru/articles/slug)"""

    def setUp(self):
        """Начальные установки"""
        self.response = self.client.get('/articles/slug-1')

    def test_uses_all_articles_template(self):
        """тест: раздел Статьи/Сатья (kiteup.ru/articles/slug)использует
        шаблон article.html"""
        self.assertTemplateUsed(self.response, 'articles/article.html')

    def test_event_uses_view_as_class_based_view(self):
        """тест: использование представления Event как Class-Based view"""
        self.assertEqual(
            self.response.resolver_match.func.__name__,
            ArticleDetailView.as_view().__name__)

    def test_display_article_title(self):
        """тест: у статьи есть заголовок"""
        self.assertContains(self.response, 'Статья 1')

    def test_display_article_author(self):
        """тест: у статьи есть автор"""
        self.assertContains(self.response, 'test')

    @skip('skip error locale output for cyrilic month')
    def test_display_article_date_publication(self):
        """тест: у статьи есть дата публикации"""
        locale.setlocale(locale.LC_ALL, 'Russian')
        date_now = time.strftime('%d %B, %Y', time.localtime())
        self.assertContains(self.response, date_now)

    def test_dysplay_article_content(self):
        """тест: собвстенно текст статьи"""
        self.assertContains(self.response,'Текст статьи')


# 1)Использовать тестовый клиент Django,
# 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
# 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
# 4) Проверить, чтобы все формы имели правильный класс.
# 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
# 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
# 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются