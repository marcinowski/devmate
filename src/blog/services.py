"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.utils import lorem_ipsum as lorem


def get_random_article():
    """ Method returns random article dictionary with content, description and title. """
    return {
        'content': lorem.paragraph(),
        'description': lorem.sentence(),
        'title': lorem.words(count=4).capitalize(),
    }
