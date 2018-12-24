from django.core.management.base import BaseCommand
from kickstart.models import kickstarter
import csv

class Command(BaseCommand):
    help = 'Load csv file.'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    kickstarter.objects.all().delete()
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            for row in reader:
                if count is 0:
                    count += 1
                    continue
                kickstarter.objects.create(
                    backers_count = row[0],
                    blurb = row[1],
                    category = row[2],
                    converted_pledged_amount = row[3]
                )
