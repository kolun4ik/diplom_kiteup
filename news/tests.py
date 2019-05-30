from django.urls import resolve
from django.test import TestCase
from news.views import index

# Create your tests here.
class HomePageTest(TestCase):
    """тест домашней страницы kiteup.ru"""

    def test_root_url_resolves_to_home_page_view(self):
        """тест: корневой url преобразуется в представление домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, index)