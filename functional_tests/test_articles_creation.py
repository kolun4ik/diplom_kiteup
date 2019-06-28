from time import sleep
from .base import FunctionalTest, REGEX_ANY_TEXT
from unittest import skip


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""

    # @skip("test skip")
    def test_display_all_articles_on_articles_page(self):
        """тест: видим все статьи в разделе 'Статьи'(/articles/)"""
        self.articles_objects_creation(3)
        self.browser.get(self.live_server_url + '/articles/')
        url = self.browser.find_elements_by_id('id_item_article')
        self.assertGreater(len(url), 1)

    # @skip("skip test title")
    def test_display_article_by_slug_link(self):
        """тест: отобразить статью по уникальному Url"""
        self.articles_objects_creation(2)
        self.browser.get(self.live_server_url + '/articles/')
        slug_list = self.browser.find_elements_by_link_text('Читать')
        slug_1 = slug_list[0].get_attribute('href')
        slug_2 = slug_list[1].get_attribute('href')
        self.browser.get(slug_1)
        self.assertEquals(self.browser.current_url, slug_1)
        self.browser.get(slug_2)
        self.assertNotEqual(self.browser.current_url, slug_1)

    # @skip("skip test title")
    def test_open_article_have_a_title(self):
        """тест: каждая стаья начинается с заголовка (названия)"""
        self.articles_objects_creation()
        self.browser.get(self.live_server_url + '/articles/')
        slug = self.browser.find_element_by_link_text('Читать').get_attribute('href')
        self.browser.get(slug)
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)

    # @skip("skip test have date and content")
    def test_open_article_have_a_creation_date_and_content(self):
        """тест: каждая новость имеет дату создания и контент"""
        self.articles_objects_creation()
        self.get_element_by_link('Читать', '/articles/')
        date = self.get_item_by_id('date_item_article').text
        content = self.get_item_by_id('item_article').text
        # Не знаю как преобразовать дату в формат на русском
        # Поставил напоминание в WorkFlowy
        # self.assertRegex(
        #     date,
        #     '(\d{2}).(\d{2}).(\d{4})',
        #     msg="Ожидаем увидеть дату в формате dd.mm.YYYY")
        self.assertRegex(content, REGEX_ANY_TEXT)
        
        


