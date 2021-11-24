
from django.views.generic import ListView

from articles.models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'articles/news.html'
    ordering = '-published_at'
