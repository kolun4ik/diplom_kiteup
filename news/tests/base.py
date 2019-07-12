from time import sleep
from django.test import TestCase
from news.models import New



class myTestCase(TestCase):
    """TestCase extended method"""

    @classmethod
    def setUpTestData(cls):
        # Создаем объекты новости для тестов
        for i in range(1, 7):
            New.objects.create(
                title=f'Новость {i}',
                description='Desc news 1',
                content=f'Lorem ipsum {i}',
                image='news\\test_news.jpg')
            sleep(0.5)