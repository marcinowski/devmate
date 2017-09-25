"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.db.models import Manager


class ArticleManager(Manager):
    def get_last_published(self, count=2):
        return self.filter(status=self.CONTENT_STATUS_PUBLISHED).order_by('publish_date')[count]
