from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article, ArticleTag, ArticleMainTag


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'
