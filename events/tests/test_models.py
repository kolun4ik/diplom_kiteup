import os
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from .base import myTestCase
from events.models import Event

class EventModelTest(myTestCase):
    """тест модели Статья"""

    def test_can_save_a_article(self):
        """тест: можно сохранить статью в БД"""
        count = Event.objects.count()
        Event.objects.create(title='Следущая статья')
        self.assertEqual(Event.objects.count(), count + 1)

    def test_events_have_date_creation(self):
        """тест: статья имеет дату создания"""
        event = Event.objects.first()
        self.assertIsInstance(event.created, datetime)

    def test_events_have_date_publication(self):
        """тест: мероприятие имеет дату публикации"""
        event = Event.objects.first()
        self.assertEqual(event.published, timezone.now().date())

    def test_events_have_content(self):
        """тест: контент мероприятия"""
        event = Event.objects.first()
        self.assertEqual(event.content, 'Текст мероприятия 1')

    def test_event_have_image(self):
        """тест: анонс мероприятия с картинкой"""
        event = Event.objects.first()
        self.assertIn('test_event_img.jpg', os.path.join(settings.STATIC_ROOT, str(event.image)))

    def test_event_have_unique_slug_url(self):
        """тест: мероприятие имет уникальный Url"""
        event1 = Event.objects.first()
        event2 = Event.objects.all()[1]
        self.assertNotEqual(event1.slug, event2.slug)

    def test_event_have_description(self):
        """тест: мероприятие имеет краткое описание длинной 100 символов"""
        event = Event.objects.first()
        self.assertEqual(event.description, 'Краткое описание мероприятия длинной 100 знаков')

    def test_event_have_visible_true_false_field(self):
        """"тест: мероприятие имеет поля, показывающее статус
        отобржения в списке: отображать/скрыть"""
        event = Event.objects.first()
        self.assertTrue(event.visible)
        event.visible = False
        self.assertFalse(event.visible)
