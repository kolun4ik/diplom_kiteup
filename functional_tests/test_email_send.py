from .base import FunctionalTest
from django.core import mail
from selenium.webdriver.common.keys import Keys
from unittest import skip


TEST_MAIL = 'test@domen.ru'
SUBJECT = 'Тест на отправку почты'


@skip('Tests skip because mail not send')
class TestEmailSend(FunctionalTest):
    """Тест отправки сообщений на почту (Контакты, регистрация и т.д.)"""

    def test_send_mail_via_contact_form(self):
        """тест: отправка сообщения на почту из контактной формы"""
        self.browser.get(self.live_server_url + '/contacts')
        input_name = self.get_item_by_id('name')
        input_email = self.get_item_by_id('email')
        input_subject = self.get_item_by_id('subject')
        input_msg = self.get_item_by_id('message')
        button = self.get_item_by_id('form-submit')

        input_name.send_keys('Joe')
        input_email.send_keys('11_ka@rambler.ru')
        input_subject.send_keys('Тест')
        input_msg.send_keys('Сообщение')
        button.send_keys(Keys.ENTER)

        self.wait_for(
            lambda: self.assertEquals(
                self.get_item_by_id('success').text,
                'Ваше сообщение успешно отравлено.'))

        email = mail.outbox[0]

        self.assertIn(input_email, email.to)
        self.assertEqual(email.subject, input_subject)
        self.assertIn(input_msg, email.body)
