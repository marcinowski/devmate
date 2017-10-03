"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
import os
import random
from django.utils import lorem_ipsum as lorem


THUMBNAILS_DIR = os.path.join('images', 'article_thumbnails')


def get_random_article():
    """ Method returns random article dictionary with content, description and title. """
    return {
        'content': lorem.paragraph(),
        'description': lorem.sentence(),
        'title': lorem.words(count=4, common=False).capitalize(),
    }


def get_random_thumbnail():
    i = random.choice(range(5))
    return os.path.join(THUMBNAILS_DIR, 'default-{}.svg'.format(i))
