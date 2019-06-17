import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from .models import ItemNews


def news_view(request, id_item):
    """представление  'Новости'"""
    if id_item == '':
        context = dict()
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