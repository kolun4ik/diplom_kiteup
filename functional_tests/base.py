import os
from time import sleep, time
from news.models import ItemNews
from pages.models import Page
from articles.models import Article
from events.models import Event
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


MAX_WAIT = 5
REGEX_ANY_TEXT = '.+'


class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""

    def setUp(self):
        """Установка, выполняется для каждого метода test_*()"""
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        """Демонтаж"""
        self.browser.quit()

    def wait_for_row_in_news_list(self, item_text):
        """Ожидание новости в таблице с новостями"""
        start_time = time()
        while True:
            try:
                list = self.browser.find_element_by_id('id_news_list')
                items = self.browser.find_elements_by_css_selector('li')
                self.assertIn(item_text, [item.text for item in items])
                return
            except (AssertionError, WebDriverException) as e:
                if time() - start_time > MAX_WAIT:
                    raise e
                sleep(0.5)

    def get_element_by_link(self, text_link, page=''):
        """Ф-ция возвращает ссылку, найденную по тексту ссылки"""
        self.browser.get(self.live_server_url + page)
        link = self.browser.find_element_by_link_text(text_link).get_attribute('href')
        self.browser.get(link)
        return link

    def wait_for(self, fn):
        """Ожидать"""
        # Явное ожидание для Selenium, для корректного обновления страницы
        # например: после отправки Keys.ENTER, чтобы оно точно попало в assert
        start_time = time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time() - start_time > MAX_WAIT:
                    raise e
                sleep(0.5)

    def get_item_by_id(self, item):
        """получить поле ввода для элемента"""
        return self.browser.find_element_by_id(item)
