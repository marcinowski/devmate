"""
:created on: 2017-09-25

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.conf import settings
from django.core.management import BaseCommand, call_command, get_commands


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Initializing data for project.')
        commands = get_commands()
        for app in settings.LOCAL_APPS:
            command = '{}_init'.format(app)
            if command in commands:
                call_command(command)
        self.stdout.write('Initializing complete.')
