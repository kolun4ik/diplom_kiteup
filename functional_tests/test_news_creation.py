from .base import FunctionalTest
from unittest import skip


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""
    @skip
    def test_can_start_a_index_page(self):
        """тест: отобразить главную страницу kiteup.ru"""
        self.browser.get(self.live_server_url)
        # Заголовок и шапка страницы говорят нам, что мы на
        # сайте kiteup.ru - 'Кайт-клуб "Вверх"'
        self.assertIn('Кайт клуб \"Вверх\"', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Кайт клуб \"Вверх\"', header_text)
        # теперь, когда мы зашли на главную страницу kiteup.ru, мы хотим
        # видеть список новостей
        self.wait_for_row_in_news_table('Новость 1')
        self.wait_for_row_in_news_table('Новость 2')


    @skip
    def test_display_all_news_in_index_page(self):
        """тест: видим все новости на главной странице"""
        # На главной странице мы видим анонсы (краткое содержание)  новостей сайта
        self.browser.get(self.live_server_url)
        url = self.browser.find_elements_by_id('id_item_news')
        # проверим что url ссылки содержит некий шаблон /club-news/
        self.assertTrue(url)
    @skip
    def test_display_all_news_in_different_urls(self):
        """тест: видим все новости в разделе /club-news/"""
        self.browser.get(self.live_server_url + '/club-news/')
        url = self.browser.find_element_by_id('id_item_news')
        # проверим что url ссылки содержит некий шаблон /club-news/
        self.assertTrue(url)

    def test_display_only_one_news(self):
        """тест: отображаем новость по ссылке"""
        # жмакаем на найденную ссылочку и убегаем на полную новость
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text('Новость 1').get_attribute('href')
        self.browser.get(link)
        self.assertEqual(self.browser.current_url, link)

    def test_one_news_have_title(self):
        """тест: каждая новость начинается с заголовка (названия) новости"""
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text('Новость 1').get_attribute('href')
        self.browser.get(link)
        header_3 = self.browser.find_element_by_tag_name('h3')
        self.assertTrue(header_3)


    # дату создания, уникальную ссылку на полную новость, кол-во просмотров и коментарии


        # тест, который никогда не срабатывает
        # self.fail('Закончить тест')