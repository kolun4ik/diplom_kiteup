import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    """тест нового пользователя"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Демонтаж"""
        # Если все так как мы хотим, закрываем броузер
        self.browser.quit()

    def check_for_row_in_news_table(self, row_text):
        """подтверждение строки в таблице с новостями"""
        table = self.browser.find_element_by_id('id_news_table')
        rows = self.browser.find_elements_by_css_selector('tr')
        self.assertIn(row_text, [row.text for row in rows])

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

        self.check_for_row_in_news_table('Новость 1')
        time.sleep(3)
        self.check_for_row_in_news_table('Новость 2')

        # тест, который никогда не срабатывает
        self.fail('Закончить тест')

        # На главной странице мы видим список новостей сайта

        # Каждая новость имеет заголовок, дату создания, кол-во просмотров и коментарии
