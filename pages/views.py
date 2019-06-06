from django.shortcuts import render
from news.models import ItemNews
# Create your views here.
def index(request):
    """домашняя сраница kiteup.ru"""
    items_news = ItemNews.objects.all()
    return render(request, 'index.html', {'items': items_news})
