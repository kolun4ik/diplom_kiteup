from django.urls import path, re_path
from .views import ArticlesListView, ArticleDetailView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles_view'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article')
]