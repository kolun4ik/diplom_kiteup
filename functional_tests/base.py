import os
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from news.models import ItemNews
from unittest import skip


MAX_WAIT = 5



class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        ItemNews.objects.create(text='Новость 1')
        ItemNews.objects.create(text='Новость 2')

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