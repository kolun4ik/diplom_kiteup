"""kiteup URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path, include
from pages import views as pages_views
from news import views as news_views
from news import urls as news_urls

urlpatterns = [
    path('', pages_views.index, name='index'),
    re_path(r'^club-news/', include(news_urls)),
    path('admin/', admin.site.urls),
]
