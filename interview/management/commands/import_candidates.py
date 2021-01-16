import csv

from django.core.management import BaseCommand

from interview.models import Candidate


class Command(BaseCommand):
    help = '從一個csv文件讀取候選人訊息，導入到資料庫裡面'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path) as file:
            csv_reader = csv.reader(file, dialect='excel')
            for row in csv_reader:
                candidate = Candidate.objects.create(
                    username=row[0],
                    city=row[1],
                    phone=row[2],
                    bachelor_school=row[3],
                    major=row[4],
                    degree=row[5]
                )
                print(candidate)
