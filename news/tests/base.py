from time import sleep
from django.test import TestCase
from news.models import ItemNews



class myTestCase(TestCase):
    """TestCase extended method"""

    @classmethod
    def setUpTestData(cls):
        # Создаем объекты новости для тестов
        for i in range(1, 7):
            ItemNews.objects.create(
                title_news=f'Новость {i}',
                content=f'Lorem ipsum {i}',
                image='\\img\\test_news.jpg')
            sleep(0.5)