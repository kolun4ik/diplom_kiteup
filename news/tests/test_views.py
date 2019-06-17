import datetime
from django.test import TestCase
from news.models import ItemNews
from time import sleep



# Create your tests here.

class NewsViewTest(TestCase):
    """тест представления новостей, раздел сайта 'Новости':
    kiteup.ru/club-news/"""

    def news_objects_creation(self, n=2):
        """Создатель новостей"""
        for i in range(1, n):
            ItemNews.objects.create(
                title_news=f'Новость {i}',
                content=f'Lorem ipsum {i}')
            sleep(0.5)


    def test_uses_news_template(self):
        """тест: раздел Новости (kiteup.ru/club-news/1)использует
        шаблон news.html"""
        news = ItemNews.objects.create(title_news='Новость 1')
        response = self.client.get(f'/club-news/{news.id}')
        self.assertTemplateUsed(response, 'news.html')


    def test_display_five_last_news_on_club_news_page(self):
        """тест: в разделе Новости отображать 5 последних новостей"""
        for i in range(6):
            ItemNews.objects.create(
                title_news=f'{i}',
                content=''
            )
        last_five = ItemNews.objects.order_by('-creation_date')[:5]
        self.assertEqual(len(last_five), 5)

    def test_display_only_item_news(self):
        """тест: отображать определенную новость по id"""
        # создаем 2 разные новости
        correct_news = ItemNews.objects.create(title_news='Новость 1')
        news2 = ItemNews.objects.create(title_news='Новость 2')
        # делаем запрос на отображение корректной новости
        response = self.client.get(f'/club-news/{correct_news.id}')

        self.assertContains(response, 'Новость 1')
        self.assertNotContains(response, 'Новость 2')

    def test_view_dispalay_date(self):
        """тест: отображать дату создания новости"""
        date = datetime.datetime.now()
        news = ItemNews.objects.create(title_news='Новость 1')
        response = self.client.get(f'/club-news/{news.id}')
        self.assertContains(response, date.strftime('%d.%m.%Y'))

    def test_display_news_content(self):
        """тест: содержимое новости"""
        news = ItemNews.objects.create(
            title_news='Новость 1',
            content = 'Lorem ipsum'
        )
        self.assertEqual('Lorem ipsum', news.content)

    def test_display_link_on_next_page_in_pagination(self):
        """тест: отображается по ссылке вида /club-news/?page=N
            страница с другим списком новостей"""
        self.news_objects_creation(7)
        count = ItemNews.objects.all().count()
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
