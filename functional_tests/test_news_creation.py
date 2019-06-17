from .base import FunctionalTest, REGEX_ANY_TEXT
from unittest import skip


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""

    # @skip("test skip")
    def test_display_free_items_news_on_club_news_page(self):
        """тест: видим 3 новости в разделе 'Новости'(/club-news/)"""
        self.news_objects_creation(5)
        self.browser.get(self.live_server_url + '/club-news/')
        url = self.browser.find_elements_by_id('id_item_news')
        self.assertEquals(len(url), 3)


    # @skip("skip test only one news")
    def test_display_only_one_news(self):
        """тест: отображаем новость по ссылке"""
        self.news_objects_creation()
        link = self.get_element_by_link('Новость 1')
        self.assertEqual(self.browser.current_url, link)


    # @skip("skip test title")
    def test_open_news_have_a_title(self):
        """тест: каждая новость начинается с заголовка (названия) новости"""
        self.news_objects_creation()
        self.get_element_by_link('Новость 1')
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)


    # @skip("skip test have date and contenx")
    def test_open_news_have_a_creation_date_and_content(self):
        """тест: каждая новость имеет дату создания и контент"""
        self.news_objects_creation()
        self.get_element_by_link('Новость 1')
        date = self.get_item_by_id('date_item_news').text
        content = self.get_item_by_id('item_news').text
        self.assertRegex(
            date,
            '(\d{2}).(\d{2}).(\d{4})',
            msg="Ожидаем увидеть дату в формате dd.mm.YYYY")
        self.assertRegex(content, REGEX_ANY_TEXT)


    def test_activation_link_page_in_pagination(self):
        """тест: активация ссылки в пагинаторе изменяет список новостей"""
        self.news_objects_creation(9)
        self.browser.get(self.live_server_url + '/club-news/')
        news_p1 = self.browser.find_element_by_id('id_item_news').text
        page_link = self.get_element_by_link('Следующая', page='/club-news/')
        self.browser.get(page_link)
        news_p2 = self.browser.find_element_by_id('id_item_news').text
        self.assertNotEqual(news_p1, news_p2)

        # Также новости могут иметь ко-во просмотров и комментарии

        # тест, который никогда не срабатывает
        # self.fail('Закончить тест')