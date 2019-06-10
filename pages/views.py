from django.shortcuts import render
from news.models import ItemNews
from .models import Pages
# Create your views here.
def index(request):
    """домашняя сраница kiteup.ru"""
    items_news = ItemNews.objects.order_by('-creation_date')[:5]
    return render(request, 'index.html', {'items': items_news})

def obuchenie(request):
    page = Pages.objects.first()
    return render(request, 'obuchenie.html', {'page': page})
