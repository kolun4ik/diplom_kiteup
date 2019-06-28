from .base import FunctionalTest, REGEX_ANY_TEXT
from unittest import skip
from events.models import Event

class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""

    # @skip("test skip")
    def test_display_all_events_on_events_page(self):
        """тест: видим все мероприятия в разделе 'Мероприятия'(/events/)"""
        self.browser.get(self.live_server_url + '/events/')
        url = self.browser.find_elements_by_id('id_item_events')
        self.assertGreater(len(url), 1)

    # @skip("skip test title")
    def test_display_event_by_slug_link(self):
        """тест: отобразить мероприятие по уникальному Url"""
        self.events_objects_creation(2)
        self.browser.get(self.live_server_url + '/events/')
        slug_list = self.browser.find_elements_by_link_text('Читать')
        slug_1 = slug_list[0].get_attribute('href')
        slug_2 = slug_list[1].get_attribute('href')
        self.browser.get(slug_1)
        self.assertEquals(self.browser.current_url, slug_1)
        self.browser.get(slug_2)
        self.assertNotEqual(self.browser.current_url, slug_1)

    # @skip("skip test title")
    def test_open_event_have_a_title(self):
        """тест: каждое мероприятие начинается с заголовка (названия)"""
        self.events_objects_creation()
        self.browser.get(self.live_server_url + '/events/')
        slug = self.browser.find_element_by_link_text('Читать').get_attribute('href')
        self.browser.get(slug)
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)

    # @skip("skip test have date and content")
    def test_open_event_have_content(self):
        """тест: каждая новость имеет дату создания и контент"""
        self.events_objects_creation()
        self.get_element_by_link('Читать', '/events/')
        content = self.get_item_by_id('item_event').text
        self.assertRegex(content, REGEX_ANY_TEXT)