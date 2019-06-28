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

    def events_objects_creation(self, n=1):
        """Создаем тестовые мероприятия"""
        for i in range(1, n+1):
            Event.objects.create(
                title=f'Мероприяте {i}',
                content='Краткое описание мероприятия',
                slug=f'slug-{i}'
            )
            # print(i)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.events_objects_creation(cls, 3)

    def setUp(self):
        """Установка, выполняется для каждого метода test_*()"""
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

        # Сгенерировали атрибуты страницы /obuchenie-kitesurfing
        Page.objects.create(
            title='Здравствуйте, мы – кайт-клуб «Вверх».',
            link='obuchenie-kitesurfing',
            body='Замена слова «школа» на «клуб» тоже неслучайна')

        # Сгенерировали атрибуты страницы /faq
        Page.objects.create(
            title='Часто задаваемые вопросы:',
            link='faq',
            body='Прежде чем звонить нам, почитайте ЧаВо...')

        # Сгенерировали атрибуты страницы /contacts
        Page.objects.create(
            title='Контакты',
            link='contacts',
            body='Информацию по всем вопросам взаимодействия Вы можете отправить, используя форму, расположенную ниже.')


    def tearDown(self):
        """Демонтаж"""
        self.browser.quit()

    def page_objects_creation(self,page):
        """Ф-ция создает main page раздел сайта"""
        Page.objects.create(
            title='Контакты',
            link='contacts',
            body='Информацию по всем вопросам взаимодействия Вы можете отправить, используя форму, расположенную ниже.')


    def news_objects_creation(self, n=1):
        """Создатель новостей"""
        for i in range(1, n+1):
            ItemNews.objects.create(
                title_news=f'Новость {i}',
                content=f'Lorem ipsum {i}')
            sleep(0.5)

    def articles_objects_creation(self, n=1):
        """Создатель статей"""
        for i in range(1, n+1):
            Article.objects.create(
                title=f'Статья {i}',
                description='Краткое описание статьи',
                content='Текст статьи',
                slug=f'slug-{i}'
            )

    def wait_for_row_in_news_table(self, item_text):
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
