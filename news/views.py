from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemNews

# Create your views here.
def index(request):
    """домашняя сраница kiteup.ru"""
    items_news = ItemNews.objects.all()
    return render(request, 'index.html', {'items': items_news})


# def view_all_news(request):
#     """представление всех новостей сайта kiteup.ru/club_news/"""
#     items_news = ItemNews.objects.all()
#     return render(request, 'club_news.html', {'items': items_news})

def news_view(request, id_item):
    """представление отдельной новости"""
    if id_item == '':
        items = ItemNews.objects.all()
        return render(request, 'club_news.html', {'items': items})
    else:
        item = ItemNews.objects.get(id=id_item)
        return  render(request, 'news.html', {'item': item})