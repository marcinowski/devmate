from django.views.generic import TemplateView

from blog.models import Article


class MainPageView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['recent_articles'] = Article.objects.get_published_recently(3)
        return context
