from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from news.views import index
from news.models import ItemNews

# Create your tests here.
class IndexPageTest(TestCase):
    """тест домашней страницы kiteup.ru"""

    def test_uses_index_template(self):
        """тест: для главной страницы используется шаблон index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class ItemModelTest(TestCase):
    """тест модели отдельно взятой новости"""

    def test_saving_and_retriving_items_news(self):
        """тест сохранения и получения отдельной взятой новости из
        таблицы новостей"""
        # код описанный ниже, скорее всего интеграциооный тест, а не модульный
        first_itemnews = ItemNews()
        first_itemnews.text = 'Новость 1'
        first_itemnews.save()

        second_itemnews = ItemNews()
        second_itemnews.text = 'Новость 2'
        second_itemnews.save()

        saved_itemnews = ItemNews.objects.all()
        self.assertEqual(saved_itemnews.count(), 2)

        first_saved_itemnews = saved_itemnews[0]
        second_saved_itemnews = saved_itemnews[1]

        self.assertEqual(first_saved_itemnews.text, 'Новость 1')
        self.assertEqual(second_saved_itemnews.text, 'Новость 2')
