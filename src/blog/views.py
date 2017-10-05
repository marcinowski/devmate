from django.views.generic import DetailView, ListView

from blog.forms import ArticleForm
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
    paginate_by = 10
    ordering = 'publish_date'

    def get_queryset(self):
        q = super().get_queryset()
        f = ArticleForm(**self.request.GET)
        f.full_clean()
        return q.filter(**f.data)
