"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.core.management import BaseCommand

from utils.services import create_test_superuser, create_test_user


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Filling in User models.')
        create_test_user()
        create_test_superuser()
