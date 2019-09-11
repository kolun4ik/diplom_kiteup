from .base import FunctionalTest
from unittest import skip


class LayoutAndStylingTest(FunctionalTest):
    """тест макета и стилевого оформления"""
    fixtures = ['pages.yaml']

    def test_page_club_news_has_paginator(self):
        """тест: на странице в в разделе 'НОВОСТИ' есть Paginator"""
        self.browser.get(self.live_server_url + '/club-news/')
        self.browser.set_window_size(1920, 1080)
        paginations = self.browser.find_element_by_css_selector('.pagination')
        self.assertTrue(paginations)
        page_link = self.browser.find_elements_by_css_selector('.page-item')
        self.assertGreater(len(page_link), 2)
        self.assertAlmostEqual(
            paginations.location['x'] + paginations.size['width'] / 2 + 140,
            960,
            delta=20
        )

    # @skip('test skip')
    def test_can_display_a_form_input_items(self):
        """тест: контактная форма должна иметь поля ввода"""
        self.browser.get(self.live_server_url + '/contacts')
        input_name = self.get_item_by_id('name')
        input_email = self.get_item_by_id('email')
        input_subject = self.get_item_by_id('subject')
        input_msg = self.get_item_by_id('message')
        button = self.get_item_by_id('form-submit')

        self.assertEquals(
            input_name.get_attribute('placeholder'),
            'Имя:')
        self.assertEquals(
            input_email.get_attribute('placeholder'),
            'Email:')
        self.assertEquals(
            input_subject.get_attribute('placeholder'),
            'Тема:')
        self.assertEquals(
            input_msg.get_attribute('placeholder'),
            'Сообщение:')
        self.assertEquals(
            button.text,
            'Отправить сообщение')
