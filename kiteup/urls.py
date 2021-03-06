"""kiteup URL Configuration"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from pages.views import NewsListView
from pages import views as pages_views
from news import urls as news_urls
from accounts import urls as accounts_urls
from articles import urls as articles_urls
from events import urls as events_urls
from filebrowser.sites import site


urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('obuchenie-kitesurfing', pages_views.obuchenie, name='obuchenie'),
    path('faq', pages_views.faq, name='faq'),
    path('contacts', pages_views.contacts, name='contacts'),
    path('club-news/', include(news_urls)),
    path('articles/', include(articles_urls)),
    path('events/', include(events_urls)),
    path('accounts/', include(accounts_urls)),
    path('admin/filebrowser/', site.urls),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
