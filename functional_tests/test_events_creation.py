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

    # @skip("skip test becose widget not exist")
    @ tag('new')
    def test_events_page_have_widget_arhive_events(self):
        """тест: на странице Мероприятия есть виджет 'Архив мероприятий'"""
        self.browser.get(self.live_server_url + '/events/')
        arhive_widget = self.browser.find_element_by_class_name('about-sidebar-widget')
        h4 = arhive_widget.find_element_by_tag_name('h4').text
        self.assertEqual(h4, 'Архив мероприятий')
        # протестировать существование виджета
        # ссылки открывают нужные формации по годам, месяцам

    def test_activation_link_page_in_pagination(self):
        """тест: активация ссылки в пагинаторе изменяет список Мероприятий"""
        self.browser.get(self.live_server_url + '/events/')
        event_p1 = self.browser.find_element_by_id('id_item_events').find_element_by_tag_name('a').text
        page_link = self.get_element_by_link('Следующая', page='/events/')
        self.browser.get(page_link)
        event_p2 = self.browser.find_element_by_id('id_item_events').find_element_by_tag_name('a').text
        self.assertNotEqual(event_p1, event_p2)
