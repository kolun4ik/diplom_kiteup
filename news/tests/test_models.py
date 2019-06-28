import datetime
from .base import myTestCase
from news.models import ItemNews


class ItemModelTest(myTestCase):
    """тест модели отдельно взятой новости"""
    def news_obj(self):
        return ItemNews.objects.first()


    def test_can_save_a_item_news(self):
        """тест: можно сохранить новость в БД"""
        count = ItemNews.objects.count()
        ItemNews.objects.create(title_news='Следущая новость')
        self.assertNotEqual(ItemNews.objects.count(), count)

    def test_news_have_date_creation(self):
        """тест: новость имеет дату создания"""
        self.assertIsInstance(self.news_obj().creation_date, datetime.datetime)

    def test_news_have_content(self):
        """тест: текст новости"""
        self.assertEqual(self.news_obj().content, 'Lorem ipsum 1')

    def test_news_have_image(self):
        """тест: каждая новость с картинкой"""
        news = self.news_obj()

