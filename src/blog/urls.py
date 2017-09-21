"""
:created on: 2017-09-21

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^/', TemplateView.as_view(), name='main')
]
