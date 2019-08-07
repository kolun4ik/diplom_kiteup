from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article
from hitcount.views import HitCountDetailView


class ArticlesListView(ListView):
    template_name = 'articles/all_articles.html'
    context_object_name = 'list_articles'

    def get_queryset(self):
        # К каждой статье выдернуть автора и счетчик просмотров
        # return Article.objects.all().order_by('-published').filter(status='published').select_related('author')
        return Article.objects.raw('''
            SELECT articles.*, hits FROM articles 
            LEFT JOIN hitcount_hit_count as hc ON hc.object_pk = articles.id 
            WHERE articles.status = 'published' 
            ORDER BY articles.published DESC
        ''')

class ArticleDetailView(HitCountDetailView):
    template_name = 'articles/article.html'
    context_object_name = 'article'
    model = Article
    count_hit = True
