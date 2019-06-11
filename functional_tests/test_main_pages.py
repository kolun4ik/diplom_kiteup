from .base import FunctionalTest, REGEX_ANY_TEXT
from unittest import skip
from time import sleep

class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""

    @skip("test skip")
    def test_can_start_a_index_page(self):
        """тест: отобразить главную страницу kiteup.ru"""
        self.browser.get(self.live_server_url)
        # Заголовок и шапка страницы говорят нам, что мы на
        # сайте kiteup.ru - 'Кайт-клуб "Вверх"'
        self.assertIn('Кайт клуб \"Вверх\"', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Кайт клуб \"Вверх\"', header_text)
        # теперь, когда мы зашли на главную страницу kiteup.ru, мы хотим
        # видеть список из 5 новостей, в порядке убывания по дате создания.
        self.wait_for_row_in_news_table('Новость 6')
        self.wait_for_row_in_news_table('Новость 5')


    @skip("test skip")
    def test_display_five_last_news_in_index_page(self):
        """тест: видим последние 5  новостей на главной странице"""
        # На главной странице мы видим анонсы (краткое содержание)  новостей сайта
        self.browser.get(self.live_server_url)
        urls = self.browser.find_elements_by_id('id_item_news')
        link = self.browser.find_element_by_link_text('Новость 6').get_attribute('href')
        regex = '/club-news/'
        # проверим что url ссылки содержит некий шаблон /club-news/
        self.assertRegex(link, regex)
        self.assertEquals(len(urls), 5)

    @skip("test skip")
    def test_can_start_a_teaching_kitesurfing_page(self):
        """тест: отобразить раздел 'КАЙТ ШКОЛА' (/obuchenie-kitesurfing)"""
        self.browser.get(self.live_server_url + '/obuchenie-kitesurfing')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        page_obuchenie = self.browser.find_element_by_id('page_content').text
        self.assertEquals(header_h2, 'Здравствуйте, мы – кайт-клуб «Вверх».')
        self.assertRegex(page_obuchenie, REGEX_ANY_TEXT)


    def test_can_start_a_faq_page(self):
        """тест: отобразить раздел 'ЧаВо?' (/faq)"""
        self.browser.get(self.live_server_url + '/faq')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        page_faq = self.browser.find_element_by_id('page_content').text
        self.assertEquals(header_h2, 'Часто задаваемые вопросы:')
        self.assertRegex(page_faq, REGEX_ANY_TEXT)