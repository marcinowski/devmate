"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.db.models import Manager


class ArticleManager(Manager):
    def get_published_recently(self, count=2):
        return self.filter(status=self.model.CONTENT_STATUS_PUBLISHED).order_by('publish_date')[:count]

    def get_published(self):
        return self.filter(status=self.model.CONTENT_STATUS_PUBLISHED)
