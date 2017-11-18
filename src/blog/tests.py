from django.contrib.auth import get_user_model
from django.test import TestCase

from blog import models as bm


User = get_user_model()


class TestManagers(TestCase):
    def setUp(self):
        self.u = User.objects.create_superuser('test', 'test@test.com', 'test')
        bm.Article.objects.create(
            status=bm.Article.CONTENT_STATUS_PUBLISHED,
            title='test',
            author=self.u
        )
        bm.Article.objects.create(
            status=bm.Article.CONTENT_STATUS_DRAFT,
            title='test_draft',
            author=self.u
        )

    def test_queryset(self):
        art = bm.Article.objects.get_published().get()
        self.assertEqual(art.title, 'test')
