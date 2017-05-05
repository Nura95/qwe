import json

from django.core.management import BaseCommand
from utils.functions import get_data
from core.models import Signal


class Command(BaseCommand):
    help = 'Add .dtu file to database'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        sig_time, sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3 = get_data(options['file_name'])
        sig_dict = {
            'time':sig_time,
            'sig_1_1': sig_1_1,
            'sig_1_3': sig_1_3,
            'sig_2_1': sig_2_1,
            'sig_2_2': sig_2_2,
            'sig_3_1': sig_3_1,
            'sig_3_3': sig_3_3
        }
        Signal.objects.create(name=options['file_name'], data=sig_dict)
