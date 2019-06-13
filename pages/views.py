from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.mail import send_mail
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
    form = ContactForm()
    context = {
        'title': page.title,
        'content': page.body,
        'success': False,
        'error': False,
        'form': form,
    }
    if request.method == 'POST':
        data = request.POST
        form = ContactForm(data=data)
        if form.is_valid():
            # Отправить Запрос на почту
            # send_mail('subject', 'body', 'from_email', ['kiteup@rambler.ru'])
            # send_mail(
            #     data['subject'],
            #     data['message'],
            #     data['email'],
            #     ['kiteup@rambler.ru'],
            #     fail_silently=False,
            # )

            context['content'] = 'Ожидайте ответа'
            context['success'] = True
            return render_to_response('contacts.html', context)
        # Если валидация не проходит, ошибки кидаем обратно в форму
        # Пока не реализовано

    return render(request, 'contacts.html', context)
