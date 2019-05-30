from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from news.views import index

# Create your tests here.
class HomePageTest(TestCase):
    """тест домашней страницы kiteup.ru"""

    def test_root_url_resolves_to_index_page_view(self):
        """тест: корневой url преобразуется в представление домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        """тест: домашняя страница возвращает правильный html"""
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Кайт-клуб \"Вверх\"</title>', html)
        self.assertTrue(html.endswith('</html>'))