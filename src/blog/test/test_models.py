"""
:created on: 2017-09-21

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.test import TestCase


from blog.models import Article
from blog.services import get_random_article
from utils.services import create_test_user


class TestArticleSlugTitle(TestCase):
    def setUp(self):
        self.article = get_random_article()
        self.user = create_test_user()

    def test_no_value(self):
        """ This test takes self.article without slug and expects slug to be created from title """
        a = Article.objects.create(author=self.user, **self.article)
        self.assertNotEqual(a.slug, '')

    def test_slug_explicit(self):
        """ This test passes slug explicitly and expects it to be this one """
        test_slug = 'test_slug'
        a = Article.objects.create(author=self.user, slug=test_slug, **self.article)
        self.assertEqual(a.slug, test_slug)
