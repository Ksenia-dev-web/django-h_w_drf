import csv

from django.core.management.base import BaseCommand
from phones.models import Phone1
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)
            for line in phone_reader:
                phone = Phone1()
                phone.name = line[1]
                # print(phone.name)
                phone.image = line[2]
                # print(phone.image)
                phone.price = line[3]
                # print(phone.price)
                phone.release_date = line[4]
                # print(phone.release_date)
                phone.lte_exists = line[5]
                phone.slug = slugify(line[1])
                # phone.save()


