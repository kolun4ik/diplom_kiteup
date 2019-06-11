from django.shortcuts import render, get_object_or_404
from news.models import ItemNews
from .models import Page
# Create your views here.

def index(request):
    """домашняя сраница kiteup.ru"""
    items_news = ItemNews.objects.order_by('-creation_date')[:5]
    return render(request, 'index.html', {'items': items_news})


def obuchenie(request):
    """страница 'КАЙТ ШКОЛА'"""
    page = get_object_or_404(Page, link='obuchenie-kitesurfing')
    context = {
        'title': page.title,
        'content': page.body,
    }
    return render(request, 'obuchenie.html', context)


def faq(request):
    """страница 'ЧаВо'"""
    page = get_object_or_404(Page, link='faq')
    context = {
        'title': page.title,
        'content': page.body,
    }
    return render(request, 'faq.html', context)


def contacts(request):
    """страница 'Контакты'"""
    page = get_object_or_404(Page, link='contacts')
    context = {
        'title': page.title,
        'content': page.body,
    }
    return render(request, 'contacts.html', context)
