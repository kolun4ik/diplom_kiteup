from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    """тест модели пользователя"""

    # def test_user_is_valid(self):
    #     #     """тест: пользователь допустим"""
    #     #     user = User(email='1@mail.ru',login='test', password='123')
    #     #     user.full_clean()