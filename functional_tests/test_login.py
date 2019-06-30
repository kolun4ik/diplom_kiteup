from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest, REGEX_ANY_TEXT
from time import sleep
USER_NAME = 'test'
PASSWORD = '123'
USER_EMAIL = '1@r.ru'

class LoginTest(FunctionalTest):
    """Тест регистрации в системе"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User.objects.create_user(username=USER_NAME, password=PASSWORD)



    def test_can_get_a_log_in(self):
        """тест: заходим на страницу авторизации
        активировав кнопку 'Войти'"""
        link_login = self.get_element_by_link('Войти')
        self.browser.get(link_login)
        self.browser.find_element_by_name('username').send_keys(USER_NAME)
        self.browser.find_element_by_name('password').send_keys(PASSWORD)
        self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertIn(
            'Защищенное пространство пользователя',
            self.browser.find_element_by_tag_name('body').text))