from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from news.views import index

# Create your tests here.
class IndexPageTest(TestCase):
    """тест домашней страницы kiteup.ru"""


    def test_uses_index_template(self):
        """тест: для главной страницы используется шаблон index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')