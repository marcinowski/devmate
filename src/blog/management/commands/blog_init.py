"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from blog.services import get_random_article
from blog.models import Article


UserModel = get_user_model()
mock_articles = [get_random_article() for _ in range(3)]


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Filling the blog models.')
        try:
            user = UserModel.objects.get(username='test')
        except UserModel.ObjectDoesNotExist:
            self.stdout.write('User `test` not found. Run `utils_init` first.')
        else:
            for mock in mock_articles:
                Article.objects.create(
                    author=user,
                    **mock,
                )
