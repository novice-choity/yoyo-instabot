import csv

from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Management command for initials requirements of the system
    """
    help = "Creation of the Country , City and Municipality"

    # A command must define handle()
    def handle(self, *args, **options):
        # with open('utils/raw_data/country.csv') as country_file:
        #     reader = csv.reader(country_file)
        #     next(reader)
        #     for row in reader:
        #         country, created = Country.objects.get_or_create(name=row[1])
        # with open('utils/raw_data/kommun.csv') as kommun_file:
        #     reader = csv.reader(kommun_file)
        #     next(reader)
        #     for row in reader:
        #         kommun, created = Municipality.objects.get_or_create(name=row[1])
        # with open('utils/raw_data/city.csv') as city_file:
        #     reader = csv.reader(city_file)
        #     next(reader)
        #     for row in reader:
        #         city, created = City.objects.get_or_create(name=row[1], country_id=1)
        self.stdout.write('Countries, Municipalities and Cities are loaded.')

        self.stdout.write('Initial data loaded successfully')
