from django.test import tag
from .base import FunctionalTest, REGEX_ANY_TEXT
from news.models import New
from unittest import skip


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""
    fixtures = ['news.yaml']

    def test_uses_fixtures_for_every_test(self):
        """тест: используем fixtures"""
        count = New.objects.all().count()
        self.assertEqual(count, 6)

    # @skip("test skip")
    def test_display_free_items_news_on_club_news_page(self):
        """тест: видим 3 новости в разделе 'Новости'(/club-news/)"""
        self.browser.get(self.live_server_url + '/club-news/')
        url = self.browser.find_elements_by_id('id_item_news')
        self.assertEquals(len(url), 3)

    # @skip("test skip")
    def test_display_every_news_item_with_preview_image(self):
        """тест: каждая новость в списки отображается с картинкой"""
        self.browser.get(self.live_server_url + '/club-news/')
        news = self.browser.find_element_by_id('id_item_news')
        image = news.find_element_by_tag_name('img')
        self.assertTrue(image)

    # @skip("test skip")
    def test_display_every_news_item_with_description(self):
        """тест: каждая новость имеет краткое описание"""
        self.browser.get(self.live_server_url + '/club-news/')
        desc = self.browser.find_element_by_class_name('card-text').text
        self.assertRegex(desc, REGEX_ANY_TEXT)
        self.assertGreater(250, len(desc))

    # @skip("skip test only one news")
    def test_display_only_one_news_by_link_on_index_page(self):
        """тест: отображаем новость по ссылке на главной странице"""
        link = self.get_element_by_link('Новость 6',)
        self.assertEqual(self.browser.current_url, link)

    # @skip("skip test only one news")
    def test_display_only_one_news_by_link_on_club_news_page(self):
        """тест: отображаем новость по ссылке 'Читать' со страницы 'Новости'"""
        link = self.get_element_by_link('Читать','/club-news/')
        self.browser.get(link)
        self.assertEqual(self.browser.current_url, link)

    # @skip("skip test title")
    def test_open_news_have_a_title(self):
        """тест: каждая новость начинается с заголовка (названия) новости"""
        self.get_element_by_link('Новость 6')
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)

    # @skip("skip test have date and contenx")
    def test_open_news_have_a_creation_date_and_content(self):
        """тест: каждая новость имеет дату создания и контент"""
        self.get_element_by_link('Новость 6')
        date = self.get_item_by_id('date_item_news').text
        content = self.get_item_by_id('item_news').text
        self.assertRegex(
            date,
            '(\d{2}).(\d{2}).(\d{4})',
            msg="Ожидаем увидеть дату в формате dd.mm.YYYY")
        self.assertRegex(content, REGEX_ANY_TEXT)

    # @skip("skip test have paginator")
    def test_activation_link_page_in_pagination(self):
        """тест: активация ссылки в пагинаторе изменяет список новостей"""
        self.browser.get(self.live_server_url + '/club-news/')
        news_p1 = self.browser.find_element_by_id('id_item_news').text
        page_link = self.get_element_by_link('Следующая', page='/club-news/')
        self.browser.get(page_link)
        news_p2 = self.browser.find_element_by_id('id_item_news').text
        self.assertNotEqual(news_p1, news_p2)

        # Также новости могут иметь ко-во просмотров и комментарии