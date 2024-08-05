from django.core.management import BaseCommand

from vitalia.management.commands.seeder_groups import Command as SeederGroups
from vitalia.management.commands.seeder_references import Command as SeederReferences


class Command(BaseCommand):
    help = "Seeder of the database. Groups and permissions are filled with data."
    SEEDERS = [SeederGroups,SeederReferences]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("SEEDER STARTED")
        for seeder in self.SEEDERS:
            seeder().handle()
        print("SEEDER FINISHED")