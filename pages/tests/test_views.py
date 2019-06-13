from django.test import TestCase
from unittest import skip
from unittest.mock import patch
from news.models import ItemNews
from pages.models import Page
from pages.forms import ContactForm
from time import sleep

POST_DATA = {
            'name': 'Joe',
            'email': 'nick@name.ru',
            'subject': 'Тест',
            'message': 'Сообщение',}

# Не забывать, что это "модульные" (интеграционные) тесты

class PageIndexViewTest(TestCase):
    """тест домашней страницы kiteup.ru"""


    def test_uses_index_template(self):
        """тест: для главной страницы используется шаблон index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


    def test_display_five_last_news_on_index_page(self):
        """тест: на Главной странице отображать 5 последних новостей"""
        for i in range(6):
            ItemNews.objects.create(
                title_news=f'{i}',
                content='Текст'
            )
        last_five = ItemNews.objects.order_by('-creation_date')[:5]
        self.assertEqual(len(last_five), 5)
        # Сделать проверку, что новости отсортированы в обратном порядке


class PageObuchenieViewTest(TestCase):
    """тест раздела 'Кайт школа'"""

    def create_page(self, title='Заголовок', link='/', body='Текст'):
        """Создает Page для тестирования"""
        # по link подумать, как сделать uniq и, чтобы он, был в urls.py
        return Page.objects.create(title=title, link=link, body=body)

    def test_display_page_content(self):
        """тест: страница отображает некий текст"""
        self.create_page(link='obuchenie-kitesurfing')
        response = self.client.get('/obuchenie-kitesurfing')
        self.assertContains(response, 'Заголовок')


    def test_uses_obuchenie_template(self):
        """для раздела КАЙТ ШКОЛА используется шаблон obuchenie.html"""
        self.create_page(link='obuchenie-kitesurfing')
        response = self.client.get('/obuchenie-kitesurfing')
        self.assertTemplateUsed(response, 'obuchenie.html')
        self.assertEqual(response.status_code, 200)



class PageFaqViewTest(TestCase):
    """тест раздела 'ЧаВо?'"""

    def create_page(self, title='Заголовок', link='/', body='Текст'):
        """Создает Page для тестирования"""
        # по link подумать, как сделать uniq и, чтобы он, был в urls.py
        return Page.objects.create(title=title, link=link, body=body)


    def test_display_page_content(self):
        """тест: страница отображает некий текст"""
        self.create_page(link='faq')
        response = self.client.get('/faq')
        self.assertContains(response, 'Заголовок')


    def test_uses_faq_template(self):
        """для раздела 'ЧаВо?' используется шаблон faq.html"""
        self.create_page(link='faq')
        response = self.client.get('/faq')
        self.assertTemplateUsed(response, 'faq.html')
        self.assertEqual(response.status_code, 200)


class PageContactsViewTest(TestCase):
    """тест раздела 'Контакты'"""

    def create_page(self, title='Заголовок', link='/', body='Текст'):
        """Создает Page для тестирования"""
        # по link подумать, как сделать uniq и, чтобы он, был в urls.py
        return Page.objects.create(title=title, link=link, body=body)


    def test_display_page_content(self):
        """тест: страница отображает некий текст"""
        self.create_page(link='contacts')
        response = self.client.get('/contacts')
        self.assertContains(response, 'Заголовок')


    def test_uses_contacts_template(self):
        """для раздела 'Контакты' используется шаблон contacts.html"""
        self.create_page(link='contacts')
        response = self.client.get('/contacts')
        self.assertTemplateUsed(response, 'contacts.html')
        self.assertEqual(response.status_code, 200)


    @skip('Skip this test')
    def test_redirect_after_POST(self):
        """тест: переадресяция после POST запроса"""
        self.create_page(link='contacts')
        response = self.client.post('/contacts', POST_DATA)
        # после отправки post запроса хотим увидеть переадресацию
        self.assertRedirects(response, '/contacts')

    # @skip('Skip this test')
    def test_display_success_mgs(self):
        """тест: отображается сообщенее об успешной отправке из формы"""
        self.create_page(link='contacts')
        response = self.client.post('/contacts', POST_DATA)
        self.assertIn('Ожидайте ответа', response.context['content'])


    # Проверить, что пустая форма не отправляется


    @skip('Skip this test because assertIsIntsnce display exeption')
    def test_contacts_page_uses_contact_form(self):
        """тест: страница 'КОНТАКТЫ' использует форму ContactForm"""
        response = self.client.get('/contacts')
        self.assertIsInstance(response.context['form'], ContactForm)


class SendContactViewTest(TestCase):
    """тест представления contacts, которое должно
        отправить сообщение на почту"""

    @skip('Skip this test')
    @patch('pages.views.send_mail')
    def test_sends_mail_to_addres_from_post(self, mock_send_mail):
        """тест: отправить данные на почту"""
        self.client.post('/contacts', POST_DATA)
        self.assertEqual(mock_send_mail.called, False)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject, 'Тест')
        self.assertEqual(from_email, 'nick@name.ru')
        self.assertEqual(to_list, ['kiteup@rambler.ru'])



# 1)Использовать тестовый клиент Django,
# 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
# 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
# 4) Проверить, чтобы все формы имели правильный класс.
# 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
# 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
# 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются