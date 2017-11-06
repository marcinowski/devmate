"""
:created on: 2017-09-21

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ArticleDetail

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)$', ArticleDetail.as_view(), name='article'),
    url(r'^(?P<id>[0-9]+)$', ArticleDetail.as_view(), name='article'),
]
