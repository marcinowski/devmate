import os
import subprocess as sub
from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        ipt = os.path.join(os.path.join(settings.BASE_DIR, "static"), 'site', 'scss', '*.scss') 
        opt = os.path.join(os.path.join(settings.BASE_DIR, "static"), 'site', 'css', 'main.css') 
        sub.run(['sass', ipt, opt], shell=True)
        call_command('runserver', *args, **options)
