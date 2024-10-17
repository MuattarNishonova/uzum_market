from  django.core.management.base import BaseCommand, CommandError

class Command (BaseCommand):
    help ="Bu sizga salom beradi"

    def handle(self):
        print('E assalomy alaykum')