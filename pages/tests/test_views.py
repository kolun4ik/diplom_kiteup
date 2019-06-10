from django.test import TestCase
from news.models import ItemNews
from pages.models import Pages
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
                content=''
            )
        last_five = ItemNews.objects.order_by('-creation_date')[:5]
        self.assertEqual(len(last_five), 5)
        # Сделать проверку, что новости отсортированы в обратном порядке


class PageObuchenieViewTest(TestCase):
    """тест раздела Кайт школа"""

    def test_uses_obuchenie_template(self):
        """для раздела КАЙТ ШКОЛА используется шаблон obuchenie.html"""
        response = self.client.get('/obuchenie-kitesurfing')
        self.assertTemplateUsed(response, 'obuchenie.html')
        self.assertEqual(response.status_code, 200)

    def test_display_page_content(self):
        """тест: страница отображает некий текст"""
        page = Pages.objects.create(
            title = 'Заголовок',
            body = 'Текст страницы',
        )
        response = self.client.get('/obuchenie-kitesurfing')
        self.assertContains(response, 'Текст страницы')





# 1)Использовать тестовый клиент Django,
# 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
# 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
# 4) Проверить, чтобы все формы имели правильный класс.
# 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
# 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
# 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются