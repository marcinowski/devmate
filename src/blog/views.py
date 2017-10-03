from django.views.generic import DetailView, ListView

from blog.models import Article


class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article.html'
    lookup_field = 'slug'
    context_object_name = 'article'


class ArticleList(ListView):
    queryset = Article.objects.get_published()
    template_name = 'blog/main.html'
    context_object_name = 'articles'
