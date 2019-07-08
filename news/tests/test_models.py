import datetime
from .base import myTestCase
from news.models import New


class NewModelTest(myTestCase):
    """тест модели отдельно взятой новости"""
    def news_obj(self):
        return New.objects.first()

    def test_can_save_a_item_news(self):
        """тест: можно сохранить новость в БД"""
        count = New.objects.count()
        New.objects.create(title='Следущая новость')
        self.assertNotEqual(New.objects.count(), count)

    def test_news_have_date_creation(self):
        """тест: новость имеет дату создания"""
        self.assertIsInstance(self.news_obj().created, datetime.datetime)

    def test_news_have_content(self):
        """тест: текст новости"""
        self.assertEqual(self.news_obj().content, 'Lorem ipsum 1')

    def test_news_have_image_preview(self):
        """тест: каждая новость с картинкой"""
        self.assertEqual(self.news_obj().image, '\\img\\test_news.jpg')
        
    def test_news_have_description(self):
        """тест: каждая новость с коротким описанием"""
        self.assertEqual(self.news_obj().description, 'Desc news 1')

