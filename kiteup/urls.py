"""kiteup URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from pages import views as pages_views
from news import urls as news_urls
from accounts import urls as accounts_urls
from articles import urls as articles_urls
from events import urls as events_urls

urlpatterns = [
    path('', pages_views.index, name='index'),
    path('obuchenie-kitesurfing', pages_views.obuchenie, name='obuchenie'),
    path('faq', pages_views.faq ,name='faq'),
    path('contacts', pages_views.contacts ,name='contacts'),
    re_path(r'^club-news/', include(news_urls)),
    re_path(r'^articles/', include(articles_urls)),
    re_path(r'^events/', include(events_urls)),
    path('accounts/', include(accounts_urls)),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/img/favicon.ico')),
    path('admin/', admin.site.urls),
]
