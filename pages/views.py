from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from news.models import ItemNews
from .models import Page
from .forms import ContactForm
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
        'success': False,
        'error': False,
        'form': ContactForm(),
    }
    if request.method == 'POST':
        name = request.POST.get('name1')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')

        context['content'] = 'Ожидайте ответа'
        context['success'] = True
        return render_to_response('contacts.html', context)

    return render(request, 'contacts.html', context)
