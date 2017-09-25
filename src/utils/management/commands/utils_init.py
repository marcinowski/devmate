"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


UserModel = get_user_model()


user = {
    'username': 'test',
    'password': 'password',
    'email': 'test@test.com',
    'first_name': 'Test',
    'last_name': 'Testy'
}

superuser = {
    'username': 'admin',
    'password': 'adminpassword',
    'email': 'admin@test.com',
    'first_name': 'Admin',
    'last_name': 'Testy'
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Filling in User models.')
        UserModel.objects.create_user(**user)
        UserModel.objects.create_superuser(**superuser)
