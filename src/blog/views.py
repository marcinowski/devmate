from django.views.generic import DetailView, ListView

from blog.forms import ArticleForm
from blog.models import Article


class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article.html'
    lookup_field = 'slug'
    context_object_name = 'article'


class ArticleList(ListView):
    model = Article
    template_name = 'blog/main.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.get_published()
