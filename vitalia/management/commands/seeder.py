from django.core.management import BaseCommand

from vitalia.management.commands.seeder_groups import Command as SeederGroups
from vitalia.management.commands.seeder_references import Command as SeederReferences
from vitalia.management.commands.seeder_cities import Command as SeederCities
from vitalia.management.commands.seeder_doctors import Command as SeederDoctors
from vitalia.management.commands.seeder_patient import Command as SeederPatient


class Command(BaseCommand):
    help = "Seeder of the database"
    SEEDERS = [SeederGroups, SeederReferences, SeederCities, SeederPatient, SeederDoctors]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Seeder started 📚")
        for seeder in self.SEEDERS:
            seeder().handle()
        print("Seeder finished 📚")