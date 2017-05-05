from django.core.management import BaseCommand
from core.models import Signal


class Command(BaseCommand):
    help = 'Add .dtu file to database'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        print(len(Signal.objects.get(id=options['id']).data['sig_1_1']))