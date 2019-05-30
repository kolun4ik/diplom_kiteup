import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    """тест нового пользователя"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Демонтаж"""
        # Если все так как мы хотим, закрываем броузер
        self.browser.quit()

    def test_can_start_a_index_page(self):
        """тест: идем на главную страницу kiteup.ru"""
        # Построим крутое функциональное приложение kiteup, перенесем старые фишечки
        # и внедрим новые. Надо очень постараться сделать все в срок, ведь это моя
        # дипломная работа на проекте otus.ru.

        # Приступаем к работе и окрываем домашнюю страничку
        self.browser.get('http://localhost:8000')

        # Заголовок и шапка страницы говорят нам, что мы на
        # сайте kiteup.ru - 'Кайт-клуб "Вверх"'
        self.assertIn('Кайт-клуб \"Вверх\"', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Кайт-клуб \"Вверх\"', header_text)

        # теперь, когда мы зашли на главную страницу kiteup.ru, мы хотим
        # увидеть список новостей в таблице
        table = self.browser.find_element_by_id('id_news_table')
        rows = self.browser.find_elements_by_css_selector('tr')
        time.sleep(3)

        self.assertIn('Новость 1', [row.text for row in rows])
        self.assertIn('Новость 2', [row.text for row in rows])
        # тест, который никогда не срабатывает
        self.fail('Закончить тест')

        # На главной странице мы видим список новостей сайта

        # Каждая новость имеет заголовок, дату создания, кол-во просмотров и коментарии

if __name__ == "__main__":
    unittest.main(warnings='ignore')