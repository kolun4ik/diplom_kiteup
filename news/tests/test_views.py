from django.test import TestCase
from news.models import ItemNews


# Create your tests here.

class NewsViewTest(TestCase):
    """тест представления новостей, раздел сайта 'Новости':
    kiteup.ru/club-news/"""
    def test_uses_news_template(self):
        """тест: раздел Новости (kiteup.ru/club-news/1)использует
        шаблон news.html"""
        news = ItemNews.objects.create(text='Новость 1')
        response = self.client.get(f'/club-news/{news.id}')
        self.assertTemplateUsed(response, 'news.html')

    def test_display_only_item_news(self):
        """тест: отображать определенную новость по id"""
        # создаем 2 разные новости
        correct_news = ItemNews.objects.create(text='Новость 1')
        news2 = ItemNews.objects.create(text='Новость 2')
        # делаем запрос на отображение корректной новости
        response = self.client.get(f'/club-news/{correct_news.id}')

        self.assertContains(response, 'Новость 1')
        self.assertNotContains(response, 'Новость 2')
