from datetime import date
from django.test import TestCase
from events.models import Event



class myTestCase(TestCase):
    """TestCase extended method"""

    @classmethod
    def setUpTestData(cls):
        for i in range(1, 4):
            Event.objects.create(
                title=f'Название мероприятия {i}',
                content=f'Текст мероприятия {i}',
                image='events\\test_event_img.jpg',
                slug=f'slug-{i}',
                description = 'Краткое описание мероприятия длинной 100 знаков',
                published=date.today(),

            )