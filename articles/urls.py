"""kiteup URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_view'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article')
]