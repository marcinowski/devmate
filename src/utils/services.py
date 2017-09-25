"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.contrib.auth import get_user_model
from utils.users_fixtures import user, superuser


UserModel = get_user_model()


def create_test_user():
    return UserModel.objects.create_user(**user)


def create_test_superuser():
    return UserModel.objects.create_superuser(**superuser)
