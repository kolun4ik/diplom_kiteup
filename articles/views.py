from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article


class ArticlesListView(ListView):
    template_name = 'all_articles.html'
    context_object_name = 'list_articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-published')


class ArticleDetailView(DetailView):
    template_name = 'article.html'
    context_object_name = 'article'
    model = Article
