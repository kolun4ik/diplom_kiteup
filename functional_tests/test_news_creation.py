from .base import FunctionalTest, REGEX_ANY_TEXT
from unittest import skip


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""

    # @skip("test skip")
    def test_display_all_news_in_different_urls(self):
        """тест: видим все новости в разделе /club-news/"""
        self.browser.get(self.live_server_url + '/club-news/')
        url = self.browser.find_element_by_id('id_item_news')
        # проверим что url ссылки содержит некий шаблон /club-news/
        self.assertTrue(url)

    # @skip("skip test only one news")
    def test_display_only_one_news(self):
        """тест: отображаем новость по ссылке"""
        link = self.get_element_by_link('Новость 3')
        self.assertEqual(self.browser.current_url, link)

    # @skip("skip test title")
    def test_one_news_have_title(self):
        """тест: каждая новость начинается с заголовка (названия) новости"""
        self.get_element_by_link('Новость 6')
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)

    # @skip("skip test have date and contenx")
    def test_one_news_have_a_creation_date_and_content(self):
        """тест: каждая новость имеет дату создания и контент"""
        self.get_element_by_link('Новость 3')
        date = self.browser.find_element_by_id('date_item_news').text
        content = self.browser.find_element_by_id('item_news').text
        self.assertRegex(date,'(\d{2}).(\d{2}).(\d{4})', msg="Ожидаем увидеть дату в формате dd.mm.YYYY")
        self.assertRegex(content, REGEX_ANY_TEXT)


        # Также новости могут иметь ко-во просмотров и комментарии

        # тест, который никогда не срабатывает
        # self.fail('Закончить тест')