"""kiteup URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path
from news import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('^club-news/(.*)$', views.view_news, name='view_news'),
]
