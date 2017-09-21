"""
:created on: 2017-09-21

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='minified')
def minified(path, ext='js'):
    """
    Filter for handling compressed files on production and keeps originals on development site.
    Note: this filter wouldn't check if the file exist! Use it only when you know when there's a compressed version.
    :param path: path to the script
    :param ext: file extension, i.e. 'js', 'css'
    :return: value.<?min.>arg

    Example of usage:
    {% static 'url/to/static/file' | minified:'js' %}
    """
    ext = ext.strip('. ')
    value = path.rstrip('. ')  # there's a chance of a file starting with a dot with a relative import
    ext = '.{}'.format(ext) if settings.DEBUG else '.min.{}'.format(ext)
    return value + ext
