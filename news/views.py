import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.dates import ArchiveIndexView
from .models import New


class NewsIndexView(ArchiveIndexView):
    model = New
    date_field = 'created'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = ''


def news_view(request, id_item):
    """представление  'Новости'"""
    if id_item == '':
        context = dict()
        items = New.objects.all().order_by('-created')
        paginator = Paginator(items, 3)
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
        return render(request, 'news/club_news.html', context)
    else:
        item = New.objects.get(id=id_item)
        created = datetime.datetime.strftime(item.created, '%d.%m.%Y')
        context = {
            'item': item,
            'date': created,
        }
        return render(request, 'news/news.html', context)
