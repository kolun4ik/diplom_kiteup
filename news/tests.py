from django.test import TestCase
from .models import ItemNews


# Create your tests here.
class IndexPageTest(TestCase):
    """тест домашней страницы kiteup.ru"""
    def test_uses_index_template(self):
        """тест: для главной страницы используется шаблон index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


class ItemModelTest(TestCase):
    """тест модели отдельно взятой новости"""
    def test_saving_and_retriving_items_news(self):
        """тест сохранения и получения отдельной взятой новости из
        таблицы новостей"""
        # код описанный ниже, скорее всего интеграциооный тест, а не модульный
        first_itemnews = ItemNews()
        first_itemnews.text = 'Новость 1'
        first_itemnews.save()

        second_itemnews = ItemNews()
        second_itemnews.text = 'Новость 2'
        second_itemnews.save()

        saved_itemnews = ItemNews.objects.all()
        self.assertEqual(saved_itemnews.count(), 2)

        first_saved_itemnews = saved_itemnews[0]
        second_saved_itemnews = saved_itemnews[1]

        self.assertEqual(first_saved_itemnews.text, 'Новость 1')
        self.assertEqual(second_saved_itemnews.text, 'Новость 2')

    def test_can_save_a_item_news(self):
        """тест: можно сохранить новость в БД"""
        # в БД еще нет новостей
        self.assertEqual(ItemNews.objects.count(),0)
        # создали новость "Новость 1"
        ItemNews.objects.create(text='Новость 1')
        self.assertEqual(ItemNews.objects.count(), 1)

        response = self.client.get('/')

        self.assertIn('Новость 1', response.content.decode('utf8'))
        self.assertTemplateUsed(response, 'index.html')



class NewsViewTest(TestCase):
    """тест представления новостей, раздел сайта 'Новости':
    kiteup.ru/club-news/"""
    def test_uses_news_template(self):
        """тест: используется шаблон новостей"""
        response = self.client.get('/club-news/')
        self.assertTemplateUsed(response, 'club_news.html')

    def test_display_all_news_items(self):
        """тест: отображать список (таблицу) всех новостей сайта"""
        ItemNews.objects.create(text='Новость 1')
        ItemNews.objects.create(text='Новость 2')

        response = self.client.get('/club-news/')

        self.assertContains(response, 'Новость 1')
        self.assertContains(response, 'Новость 1')
