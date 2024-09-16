from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from authentication.models import User
from doctors.models.city import City


class Command(BaseCommand):
    help = "Seeder of the database. Admin table is filled with data."
    ADMINS = [{
            "first_name": "Admin",
            "last_name": "Vitalia",
            "username": "adminvitalia",
            "email": "admin.admin@vitalia.com",
            "phone": "666555444",
            "password": "qwerty",
            "city_id": 1,
            "genre": "Varon",
            "birth_date": "1990-01-01",
            "identification_number": "12345678A",
            "is_staff": True,
            "is_superuser": True,
        }]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Creating admins 👨‍⚕️')
        for admin_data in self.ADMINS:
            try:
                city = City.objects.get(id = admin_data["city_id"])
                role = Group.objects.get(name = "Admin")

                if User.objects.filter(username = admin_data["username"]).exists():
                    print(f"User {admin_data['username']} already exists, skipping.")
                    continue

                user = User.objects.create_user(
                        first_name = admin_data["first_name"],
                        last_name = admin_data["last_name"],
                        username = admin_data["username"],
                        email = admin_data["email"],
                        phone = admin_data["phone"],
                        city = city,
                        identification_number = admin_data["identification_number"],
                        genre = admin_data["genre"],
                        birth_date = admin_data["birth_date"],
                        password = admin_data["password"],
                        is_staff = admin_data["is_staff"],
                        is_superuser = admin_data["is_superuser"]
                        )
                user.groups.add(role)
                user.save()
                print(f"Admin {admin_data['username']} created successfully")
            except City.DoesNotExist:
                print(f"City with ID {admin_data['city_id']} does not exist")
            except Exception as e:
                print(f"An error occurred: {e}")
        print("Ending patient creation 👋")
