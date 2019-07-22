import os
from datetime import datetime, date
from django.utils import timezone
from django.conf import settings
from .base import myTestCase
from events.models import Event

class EventModelTest(myTestCase):
    """тест модели Статья"""

    def last(self):
        """Выбираем атрибуты первого мероприятия"""
        return Event.objects.last()

    def test_can_save_a_article(self):
        """тест: можно сохранить статью в БД"""
        count = Event.objects.count()
        Event.objects.create(title='Следущая статья')
        self.assertEqual(Event.objects.count(), count + 1)

    def test_event_have_date_creation(self):
        """тест: статья имеет дату создания"""
        self.assertIsInstance(self.last().created, datetime)

    def test_event_have_date_publication(self):
        """тест: мероприятие имеет дату публикации"""
        self.assertIsInstance(self.last().published, date)

    def test_event_have_date_updated(self):
        """тест: мероприятие имеет дату изменения"""
        self.assertIsInstance(self.last().updated, datetime)

    def test_event_have_title(self):
        """тест: у мероприятия есть заголовок """
        self.assertEqual(self.last().title, 'Мероприятие 1')

    def test_event_have_content(self):
        """тест: контент мероприятия"""
        self.assertEqual(self.last().content, 'Текст мероприятия 1')

    def test_event_have_image(self):
        """тест: анонс мероприятия с картинкой"""
        self.assertIn(
            'test_event_img.jpg',
            os.path.join(
                settings.STATIC_ROOT,
                str(self.last().image)))

    def test_event_have_unique_slug_url(self):
        """тест: мероприятие имет уникальный Url"""
        event1 = Event.objects.all()[0]
        event2 = Event.objects.all()[1]
        self.assertNotEqual(event1.slug, event2.slug)

    def test_event_have_description(self):
        """тест: мероприятие имеет краткое описание длинной 100 символов"""
        self.assertEqual(self.last().description, 'Краткое описание мероприятия 1')

    def test_event_have_visible_true_false_field(self):
        """"тест: мероприятие имеет поля, показывающее статус
        отобржения в списке: отображать/скрыть"""
        event = Event.objects.first()
        self.assertTrue(event.visible)
        event.visible = False
        self.assertFalse(event.visible)
