from .base import FunctionalTest, REGEX_ANY_TEXT
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from unittest import skip


class ContactFormTest(FunctionalTest):
    """Тест формы в разделе 'КОНТАКТЫ'"""

    def test_can_send_fill_form_items(self):
        """тест: заполняем поля формы и отправляем в action, хотим
            видеть сообщение об успешной отправке"""
        self.browser.get(self.live_server_url + '/contacts')
        input_name = self.get_item_by_id('name')
        input_email = self.get_item_by_id('email')
        input_subject = self.get_item_by_id('subject')
        input_msg = self.get_item_by_id('message')
        button = self.get_item_by_id('form-submit')

        input_name.send_keys('Joe')
        input_email.send_keys('11_ka@rambler.ru')
        input_subject.send_keys('Тест')
        input_msg.send_keys('Сообщение')
        button.send_keys(Keys.ENTER)

        # Здесь мы хотим увидеть респонс об успешной отправке
        self.wait_for(
            lambda: self.assertEquals(
                self.get_item_by_id('success').text,
                'Ваше сообщение успешно отравлено.'))

    def test_cannot_send_empy_feild_of_form(self):
        """тест: форма не отправляет пустые поля"""
        self.browser.get(self.live_server_url + '/contacts')

        # Убедиться что элемент стал .visible
        self.get_item_by_id('name').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertTrue(
            self.browser.find_elements_by_css_selector('.with-errors')[0].is_displayed()
        ))

        self.get_item_by_id('email').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertTrue(
            self.browser.find_elements_by_css_selector('.with-errors')[1].is_displayed()
        ))

        self.get_item_by_id('subject').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertTrue(
            self.browser.find_elements_by_css_selector('.with-errors')[2].is_displayed()
        ))
        # textarea почему-то не реагирует на нажатие ENTER выводом сообщения
        # self.get_item_by_id('message').send_keys(Keys.ENTER)
        # self.wait_for(lambda: self.assertTrue(
        #     self.browser.find_elements_by_css_selector('.with-errors')[3].is_displayed()
        # ))

        # форма не должна отправиться
        self.get_item_by_id('form-submit').send_keys(Keys.ENTER)

        with self.assertRaisesRegex(
                NoSuchElementException,
                '[id="success"]'):
            self.browser.find_element_by_id('success')

