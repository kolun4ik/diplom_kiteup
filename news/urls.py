"""kiteup URL Configuration"""
from django.urls import path, re_path
from news import views

urlpatterns = [
    re_path(r'^(.*)$', views.news_view, name='news_view'),
]
