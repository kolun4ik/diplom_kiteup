"""kiteup URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path
from news import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club-news/', views.view_all_news, name='view_all_news'),
]
