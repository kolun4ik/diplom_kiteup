from django.test import TestCase
from pages.models import Page

class PagesModelTest(TestCase):
    """тест модели страниц"""

    def test_can_save_pages_attribute(self):
        """тест: сохраняем атрибуты страницы /в БД"""
        self.assertEqual(Page.objects.count(), 0)
        Page.objects.create(
            title='Страница 1',
            link='obuchenie-kitesurfing',
            body='Текст страницы 1')
        self.assertEqual(Page.objects.count(), 1)
        response = self.client.get('/obuchenie-kitesurfing')
        self.assertIn('Страница 1', response.content.decode('utf8'))
        self.assertIn('Текст страницы 1', response.content.decode('utf8'))

