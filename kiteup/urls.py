"""kiteup URL Configuration"""
from django.urls import path, re_path
from news import views

urlpatterns = [
    path('', views.index, name='index'),
]
