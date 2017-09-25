from django.views.generic import DetailView, ListView

from blog.models import Article


class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'


class ArticlesView(ListView):
    queryset = Article.archive.get_last_published()
