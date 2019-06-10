import os
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from news.models import ItemNews
from pages.models import Pages
from unittest import skip


MAX_WAIT = 5
REGEX_ANY_TEXT = '.+'



class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        # Сгенерировали новости
        for i in range(1,7):
            ItemNews.objects.create(
                title_news=f'Новость {i}',
                content='Lorem ipsum')
        # Сгенерировали атрибуты страницы
        Pages.objects.create(
            title='Здравствуйте, мы – кайт-клуб «Вверх».',
            body='Test')

    def tearDown(self):
        """Демонтаж"""
        self.browser.quit()

    def wait_for_row_in_news_table(self, item_text):
        """Ожидание новости в таблице с новостями"""
        start_time = time.time()
        while True:
            try:
                list = self.browser.find_element_by_id('id_news_list')
                items = self.browser.find_elements_by_css_selector('li')
                self.assertIn(item_text, [item.text for item in items])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def get_element_by_link(self, text_link):
        """Ф-ция возвращает ссылку, найденную по тексту ссылки"""
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text(text_link).get_attribute('href')
        self.browser.get(link)
        return link