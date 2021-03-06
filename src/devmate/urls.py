"""devmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url, static, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import MainPageView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^o-mnie/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^projekty/', TemplateView.as_view(template_name='projects.html'), name='projects'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
