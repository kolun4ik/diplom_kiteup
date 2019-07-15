from unittest import skip
from .base import myTestCase
from news.models import New


class ClubNewsViewTest(myTestCase):
    """тест представления  'Новости'(kiteup.ru/club-news/)"""

    def setUp(self):
        self.response = self.client.get('/club-news/')

    def test_uses_club_news_template(self):
        """тест: раздел 'Новости' (kiteup.ru/club-news/) использует
        шаблон club_news.html"""
        self.assertTemplateUsed(self.response, 'club_news.html')

    # @skip('skip test')
    def test_display_free_last_news_on_club_news_page(self):
        """тест: в разделе Новости отображать 3 последних новостей"""
        # Пагинацией управляет Paginator, и он разбивает новости
        # по три на каждой странице. Надо вытащить настройки из
        # пагинатора, и их сравнить.
        paginator = self.response.context['items']
        self.assertEqual(str(paginator), '<Page 1 of 2>')

    # @skip('skip test')
    # def test_display_item_in_news_list_have_image(self):
    #     """тест: каждый пункт новости из превью отображается с картинкой"""
        # Не знаю как вытащить картинку в Response client()
        # image = self.response.context['items']
        # self.assertTrue(image)

    # def test_every_item_in_news_list_have_description_lt_100_symbols(self):
    #     """тест: у новости в списке новосте есть описание не юолее 100 символов"""
    #     desc = self.response.context['items']



class NewsViwsTest(myTestCase):
    """тест представления  'Новости/Новость' (kiteup.ru/club-news/id_news)"""

    def setUp(self):
        self.response = self.client.get('/club-news/1')

    def test_uses_news_template(self):
        """тест: раздел Новости/Новость (kiteup.ru/club-news/id_news)
            использует шаблон news.html"""
        self.assertTemplateUsed(self.response, 'news.html')

    # @skip('skip test')
    def test_display_only_item_news(self):
        """тест: отображать определенную новость по id"""
        news_1 = New.objects.all()[0]
        response = self.client.get(f'/club-news/{news_1.id}')
        self.assertContains(response, 'Новость 1')
        self.assertNotContains(response, 'Новость 2')

    # @skip('skip test')
    def test_view_dispalay_date(self):
        """тест: отображать дату создания новости"""
        data_firts_news = '25.06.2019'
        self.assertContains(self.response, data_firts_news)

    # @skip('skip test')
    def test_display_news_content(self):
        """тест: содержимое новости"""
        self.assertContains(self.response, 'Новость 1')
        self.assertNotContains(self.response, 'Новость 2')

    # @skip('skip test')
    def test_display_link_on_next_page_in_pagination(self):
        """тест: отображается по ссылке вида /club-news/?page=N
            страница с другим списком новостей"""
        count = New.objects.all().count()
        page_number = count // 3
        response = self.client.get(f'/club-news/?page={page_number}')
        self.assertContains(response, 'Новость 1')


    # 1)Использовать тестовый клиент Django,
    # 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
    # 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
    # 4) Проверить, чтобы все формы имели правильный класс.
    # 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
    # 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
    # 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются
