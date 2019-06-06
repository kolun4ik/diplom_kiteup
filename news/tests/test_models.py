from django.test import TestCase
from news.models import ItemNews


class ItemModelTest(TestCase):
    """тест модели отдельно взятой новости"""
    def test_saving_and_retriving_items_news(self):
        """тест сохранения и получения отдельной взятой новости из
        таблицы новостей"""
        # код описанный ниже, скорее всего интеграциооный тест, а не модульный
        first_itemnews = ItemNews()
        first_itemnews.title_news = 'Новость 1'
        first_itemnews.save()

        second_itemnews = ItemNews()
        second_itemnews.title_news = 'Новость 2'
        second_itemnews.save()

        saved_itemnews = ItemNews.objects.all()
        self.assertEqual(saved_itemnews.count(), 2)

        first_saved_itemnews = saved_itemnews[0]
        second_saved_itemnews = saved_itemnews[1]

        self.assertEqual(first_saved_itemnews.title_news, 'Новость 1')
        self.assertEqual(second_saved_itemnews.title_news, 'Новость 2')

    def test_can_save_a_item_news(self):
        """тест: можно сохранить новость в БД"""
        self.assertEqual(ItemNews.objects.count(),0)
        # создали новость "Новость 1"
        ItemNews.objects.create(title_news='Новость 1')
        self.assertEqual(ItemNews.objects.count(), 1)

        response = self.client.get('/')

        self.assertIn('Новость 1', response.content.decode('utf8'))
        self.assertTemplateUsed(response, 'index.html')





