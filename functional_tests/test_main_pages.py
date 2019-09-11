from .base import FunctionalTest, REGEX_ANY_TEXT
from selenium.webdriver.common.keys import Keys
from unittest import skip
from news.models import New


class NewVisitorTest(FunctionalTest):
    """тест новый посетитель"""
    fixtures = ['news.yaml', 'pages.yaml', 'articles.yaml', 'users.yaml']

    # @skip("test skip")
    def test_can_start_a_index_page(self):
        """тест: отобразить главную страницу kiteup.ru"""
        self.browser.get(self.live_server_url)
        self.assertIn('Кайт клуб \"Вверх\"', self.browser.title)
        self.wait_for_row_in_news_list('Новость 6')
        self.wait_for_row_in_news_list('Новость 5')

    # @skip("test skip")
    def test_display_five_last_news_in_index_page(self):
        """тест: видим последние 5  новостей на главной странице"""
        self.browser.get(self.live_server_url)
        urls = self.browser.find_elements_by_id('id_item_news')
        link = self.browser.find_element_by_link_text('Новость 6').get_attribute('href')
        regex = '/club-news/'
        self.assertRegex(link, regex)
        self.assertEquals(len(urls), 5)

    # @skip("test skip")
    def test_can_start_a_teaching_kitesurfing_page(self):
        """тест: отобразить раздел 'КАЙТ ШКОЛА' (/obuchenie-kitesurfing)"""
        self.browser.get(self.live_server_url + '/obuchenie-kitesurfing')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        page_obuchenie = self.get_item_by_id('page_content').text
        self.assertEquals(header_h2, 'Здравствуйте, мы – кайт-клуб «Вверх».')
        self.assertRegex(page_obuchenie, REGEX_ANY_TEXT)

    # @skip("test skip")
    def test_can_start_a_faq_page(self):
        """тест: отобразить раздел 'ЧаВо?' (/faq)"""
        self.browser.get(self.live_server_url + '/faq')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        page_faq = self.get_item_by_id('page_content').text
        self.assertEquals(header_h2, 'Часто задаваемые вопросы:')
        self.assertRegex(page_faq, REGEX_ANY_TEXT)

    # @skip("test skip")
    def test_can_start_articles_page(self):
        """тест: отобразить раздел 'Статьи'(/articles)"""
        self.browser.get(self.live_server_url + '/articles/')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        page_articles = self.browser.find_elements_by_id('id_item_article')
        self.assertEquals(header_h2, 'Статьи')
        self.assertGreater(len(page_articles), 0)

    # @skip("test skip")
    def test_can_start_a_contacts_page(self):
        """тест: отобразить раздел 'Контакты' (/contacts)"""
        self.browser.get(self.live_server_url + '/contacts')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        page_cont = self.get_item_by_id('page_content').text
        self.assertEquals(header_h2, 'Контакты')
        self.assertRegex(page_cont, REGEX_ANY_TEXT)

    # @skip("test skip")
    def test_can_start_a_login_page(self):
        """тест: отобразить раздел для авторизации"""
        self.browser.get(self.live_server_url)
        link_login = self.get_element_by_link('Войти')
        self.browser.get(link_login)
        form = self.browser.find_element_by_tag_name('form')
        self.assertTrue(form)

    # @skip("test skip")
    def test_can_start_a_dashboard_page(self):
        """тест: отобразить личный кабинет пользователя"""
        self.browser.get(self.live_server_url + '/accounts/dashboard')
        header_h3 = self.browser.find_element_by_tag_name('h3').text
        self.assertEquals(header_h3, 'Личный кабинет пользователя')

    # @skip("test skip")
    def test_can_start_a_events_page(self):
        """тест: отобразить раздел 'События' (/events/)"""
        self.browser.get(self.live_server_url + '/events')
        header_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertEquals(header_h2, 'Мероприятия')
