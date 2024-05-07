import csv
from django.core.management.base import BaseCommand
from dashboard.models import * # Adjust "yourapp" to the name of your Django app

class Command(BaseCommand):
    help = 'Load respondents from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        with open(csv_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                country = Country.objects.get(title=row['country'])
                area = Area.objects.get(title=row['area']) if row['area'].strip() else None
                gender = Gender.objects.get(title=row['gender'])
                generation = Generation.objects.get(title=row['generation'])
                resp = RespAcq.objects.get(title=row['res_acq'])
                foodstyle = FoodStyle.objects.get(title=row['foodstyle'])
                food = Food.objects.get(title=row['product_name'])
                frequency = Frequency.objects.get(title=row['freq']) if row['freq'].strip() else None
                growthrate = GrowthRate.objects.get(title=row['q5']) if row['q5'].strip() else None

                Respondent.objects.create(
                    id_num=row['id_num'],
                    country=country,
                    area=area,
                    gender=gender,
                    generation=generation,
                    resp=resp,
                    foodstyle=foodstyle,
                    food=food,
                    frequency=frequency,
                    growthrate=growthrate,
                )
        self.stdout.write(self.style.SUCCESS('Successfully populated respondents'))