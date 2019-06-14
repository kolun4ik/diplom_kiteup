import datetime
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import ItemNews

# Create your views here.
# def view_all_news(request):
#     """представление всех новостей сайта kiteup.ru/club_news/"""
#     items_news = ItemNews.objects.all()
#     return render(request, 'club_news.html', {'items': items_news})

def news_view(request, id_item):
    """представление отдельной новости"""
    if id_item == '':
        items = ItemNews.objects.all().order_by('-creation_date')
        paginator = Paginator(items,3)
        page = request.GET.get('page')
        try:
            # Если страница существует, то выбираем ее
            context = {
                'items': paginator.page(page),
            }
        except PageNotAnInteger:
            context = {
                'items': paginator.page(1),
            }
        except EmptyPage:
            context = {
                'items': paginator.page(paginator.num_pages),
            }
        return render(request, 'club_news.html', context)
    else:
        item = ItemNews.objects.get(id=id_item)
        creation_date = datetime.datetime.strftime(item.creation_date, '%d.%m.%Y')
        context = {
            'item': item,
            'date': creation_date,
        }
        return  render(request, 'news.html', context)