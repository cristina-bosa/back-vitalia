from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand, CommandError

from doctors.models.city import City
from doctors.models.specialty import Specialty
from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_history import MedicalHistory
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases


class Command(BaseCommand):
    help = "Seeder of the database. Groups and permissions are filled with data."
    GROUPS = ["Admin", "Doctor", "Patient"]
    PERMISSIONS_TO_IGNORE = {
        GROUPS[0]: { # ADMIN
            'add': [],
            'change': [],
            'delete': [],
            'view': [],
            'model': [],
            'ignore': []
        },
        GROUPS[1]: { # DOCTOR
            'add': [],
            'change': [],
            'delete': [],
            'view': [],
            'model': [],
            'ignore': []
        },
        GROUPS[2]: { # PATIENT
            'add': [],
            'change': [],
            'delete': [],
            'view': [],
            'model': [],
            'ignore': []
        },
    }

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("SEEDER STARTED")
        print("Creating groups")
        for group in self.GROUPS:
            try:
                Group.objects.create(name=group)
                print(f"{group} created")
            except Exception as e:
                pass

        print("\nAssign permissions to groups")
        for group_name in self.GROUPS:
            group = Group.objects.get(name=group_name)
            permissions_rules = self.PERMISSIONS_TO_IGNORE[group_name]
            for permission in Permission.objects.all():
                try:
                    perm_type, perm_model = permission.codename.split('_')[0], permission.content_type.model
                    rules = permissions_rules.get(perm_type, [])
                    if any([
                        perm_model in rules,
                        perm_model in permissions_rules['model'],
                        permission.codename in permissions_rules['ignore']
                    ]):
                        continue
                    group.permissions.add(permission)
                    print(f"{permission} added to {group}")
                except Exception as e:
                    pass

        print("SEEDER FINISHED")