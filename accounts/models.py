from django.db import models

# Create your models here.
# class User(models.Model):
#     """Пользователь"""
#     login = models.CharField(max_length=12)
#     name = models.CharField(max_length=20, blank=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=40,blank=False)
#     avatar = models.ImageField(blank=True)
#     date_registration = models.DateTimeField(auto_now=True)
#
#     REQUIRED_FIELDS = []
#     USERNAME_FIELD = 'email'
#     is_anonymous = False
#     is_authenticated = False
