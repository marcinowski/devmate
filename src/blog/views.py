from django.views.generic import DetailView

from blog.models import Article


class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'
