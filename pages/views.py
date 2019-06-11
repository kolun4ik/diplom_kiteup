from django.shortcuts import render
from news.models import ItemNews
from .models import Page
# Create your views here.

def index(request):
    """домашняя сраница kiteup.ru"""
    items_news = ItemNews.objects.order_by('-creation_date')[:5]
    return render(request, 'index.html', {'items': items_news})


def obuchenie(request):
    """страница 'КАЙТ ШКОЛА'"""
    page = Page.objects.first()
    return render(request, 'obuchenie.html', {'page': page})


def faq(request):
    """страница 'ЧаВо'"""
    # page = Page.objects.get(link='/faq')
    # УЖАСНЫЙ ГОВНОКОД, но пока ничего не придумал, время поджимает
    context = {
        'title': 'Часто задаваемые вопросы:',
        'content': 'Прежде чем звонить нам, почитайте ЧаВо – вполне возможно, что ответ на ваш вопрос здесь уже есть.'
    }
    return render(request, 'faq.html', context)
