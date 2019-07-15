from .base import myTestCase
from events.views import EventsListView, EventDetailView
from unittest import skip

# @skip('Skip Class')
class EventsViewTest(myTestCase):
    """тест представления мероприятий, раздел сайта 'Мероприятия'
    (kiteup.ru/events/)"""

    def setUp(self):
        """Начальные установки"""
        self.response = self.client.get('/events/')

    def test_uses_all_events_template(self):
        """тест: раздел Мероприятия (kiteup.ru/events/)
         использует шаблон all_events.html"""
        self.assertTemplateUsed(self.response, 'all_events.html')

    def test_events_uses_view_as_class_based_view(self):
        """тест: использование представления Events как Class-Based view"""
        self.assertEqual(
            self.response.resolver_match.func.__name__,
            EventsListView.as_view().__name__)

    def test_display_all_last_articles_on_articles_page(self):
        """тест: в разделе Мероприятия отображать все статьи"""
        count = len(self.response.context['list_events'])
        self.assertGreater(count, 1)

# @skip('Skip Class')
class EventViewTest(myTestCase):
    """тест представления Мероприятие , раздел сайта 'Мероприятия/Мероприятие'
    (kiteup.ru/events/slug)"""

    def setUp(self):
        """Начальные установки"""
        self.response = self.client.get('/events/slug-1')

    def test_uses_all_articles_template(self):
        """тест: раздел Мероприятия/Мероприятие (kiteup.ru/events/slug) использует
        шаблон event.html"""
        self.assertTemplateUsed(self.response, 'event.html')

    def test_event_uses_view_as_class_based_view(self):
        """тест: использование представления Event как Class-Based view"""
        self.assertEqual(
            self.response.resolver_match.func.__name__,
            EventDetailView.as_view().__name__)

    def test_display_event_title(self):
        """тест: у мероприятия есть заголовок"""
        self.assertContains(self.response, 'Мероприятие 1')

    def test_dysplay_event_content(self):
        """тест: собвстенно текст статьи"""
        self.assertContains(self.response,'Текст мероприятия 1')

