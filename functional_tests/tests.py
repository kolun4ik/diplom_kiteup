import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from news.models import ItemNews

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
    """тест нового пользователя"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()
        ItemNews.objects.create(text='Новость 1')
        ItemNews.objects.create(text='Новость 2')

    def tearDown(self):
        """Демонтаж"""
        # Если все так как мы хотим, закрываем броузер
        self.browser.quit()

    def wait_for_row_in_news_table(self, row_text):
        """Ожидание новости в таблице с новостями"""
        start_time = time.time()

        while True:
            try:
                table = self.browser.find_element_by_id('id_news_table')
                rows = self.browser.find_elements_by_css_selector('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_index_page(self):
        """тест: идем на главную страницу kiteup.ru"""
        # Построим крутое функциональное приложение kiteup, перенесем старые фишечки
        # и внедрим новые. Надо очень постараться сделать все в срок, ведь это моя
        # дипломная работа на проекте otus.ru.
        # Приступаем к работе и окрываем домашнюю страничку
        self.browser.get(self.live_server_url)
        # Заголовок и шапка страницы говорят нам, что мы на
        # сайте kiteup.ru - 'Кайт-клуб "Вверх"'
        self.assertIn('Кайт-клуб \"Вверх\"', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Кайт-клуб \"Вверх\"', header_text)
        # теперь, когда мы зашли на главную страницу kiteup.ru, мы хотим
        # увидеть список новостей в таблице
        # перешли на LiveServerTestCase, который создает свою БД и
        # удаляет ее после отработки тестов. Новости снова не выдны
        self.wait_for_row_in_news_table('Новость 1')
        self.wait_for_row_in_news_table('Новость 2')


        # На главной странице мы видим анонсы (краткое содержание)  новостей сайта
    def test_dispplay_all_news_in_index_page(self):
        """тест: видим все новости на главной странице"""
        self.browser.get(self.live_server_url)
        url = self.browser.find_element_by_id('id_item_news')
        # проверим что url ссылки содержит некий шаблон /club-news/
        self.assertTrue(url)

    def test_display_all_news_in_different_urls(self):
        """тест: видим все новости в разделе /club-news/"""
        self.browser.get(self.live_server_url + '/club-news/')
        url = self.browser.find_element_by_id('id_item_news')
        # проверим что url ссылки содержит некий шаблон /club-news/
        self.assertTrue(url)

    # def test_activate_link_on_anons_news(self):
    #     """тест: переход по ссылке в новости"""
    #     # жмакаем на найденную ссылочку и убегаем на полную новость
    #     response = self.browser.get(self.live_server_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['location'], '/club-news/news_1')

        # Каждый анонс имеет заголовок, дату создания, уникальную ссылку на полную новость, кол-во просмотров и коментарии

        # тест, который никогда не срабатывает
        # self.fail('Закончить тест')