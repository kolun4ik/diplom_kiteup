from django.test import tag
from unittest import skip
from .base import FunctionalTest, REGEX_ANY_TEXT


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""
    fixtures = ['events.yaml']

    # @skip("test skip")
    def test_display_five_events_on_events_page(self):
        """тест: видим 5 последних мероприятия в разделе 'Мероприятия'(/events/)"""
        self.browser.get(self.live_server_url + '/events/')
        url = self.browser.find_elements_by_id('id_item_events')
        self.assertEqual(len(url), 5)

    # @skip("skip test title")
    def test_display_event_by_slug_link(self):
        """тест: отобразить мероприятие по уникальному Url"""
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
        self.browser.get(self.live_server_url + '/events/')
        slug = self.browser.find_element_by_link_text('Читать').get_attribute('href')
        self.browser.get(slug)
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)

    # @skip("skip test have date and content")
    def test_open_event_have_content(self):
        """тест: каждое мероприятие имеет контент"""
        self.get_element_by_link('Читать', '/events/')
        content = self.get_item_by_id('item_event').text
        self.assertRegex(content, REGEX_ANY_TEXT)

    @skip("skip test becose widget not exist")
    def test_events_page_have_widget_arhive_events(self):
        """тест: на странице Мероприятия есть виджет 'Архив мероприятий'"""
        self.browser.get(self.live_server_url + '/events/')
        # протестировать существование виджета
        # ссылки открывают нужные формации по годам, месяцам
