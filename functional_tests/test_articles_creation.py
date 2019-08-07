from django.test import tag
from .base import FunctionalTest, REGEX_ANY_TEXT
from unittest import skip


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""
    fixtures = ['articles.yaml','users.yaml']

    # @skip("test skip")
    def test_display_all_articles_on_articles_page(self):
        """тест: видим все статьи в разделе 'Статьи'(/articles/)"""
        self.browser.get(self.live_server_url + '/articles/')
        url = self.browser.find_elements_by_id('id_item_article')
        self.assertGreater(len(url), 1)

    # @skip("test skip")
    def test_display_every_article_item_with_preview_image(self):
        """тест: каждая статьая в списки отображается с картинкой 233x233"""
        self.browser.get(self.live_server_url + '/articles/')
        news = self.browser.find_element_by_id('id_item_article')
        image = news.find_element_by_tag_name('img')
        self.assertTrue(image)

    # @tag('new')
    def test_display_every_article_item_with_description(self):
        """тест: каждая статья имеет краткое описание"""
        self.browser.get(self.live_server_url + '/articles/')
        desc = self.browser.find_element_by_class_name('description').text
        self.assertRegex(desc, REGEX_ANY_TEXT)
        self.assertGreater(250, len(desc))

    # @skip("skip test title")
    def test_display_article_by_slug_link(self):
        """тест: отобразить статью по уникальному Url"""
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
        self.browser.get(self.live_server_url + '/articles/')
        slug = self.browser.find_element_by_link_text('Читать').get_attribute('href')
        self.browser.get(slug)
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertRegex(header_h3, REGEX_ANY_TEXT)

    # @skip("skip test have date and content")
    def test_open_article_have_a_creation_date_and_content(self):
        """тест: каждая новость имеет дату создания и контент"""
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

    # @skip("skip test have date and content")
    def test_article_have_hit_counter(self):
        """тест: каждая статья имеет счетчик просмотров"""
        #XPath: /html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[3]/span[2]
        self.browser.get(self.live_server_url + '/articles/')
        hit_count_1 = self.browser.find_element_by_xpath('//div[@class="card-2"]/div[@class="extra"]/span[2]').text
        slug = self.browser.find_element_by_link_text('Читать').get_attribute('href')
        self.browser.get(slug)
        self.browser.get(self.live_server_url + '/articles/')
        hit_count_2 = self.browser.find_element_by_xpath('//div[@class="card-2"]/div[@class="extra"]/span[2]').text
        self.assertGreater(hit_count_2, hit_count_1)

        


