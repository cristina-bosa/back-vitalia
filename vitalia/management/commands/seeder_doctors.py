from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from authentication.models.doctor import Doctor
from authentication.models.user import User
from doctors.models.city import City
from doctors.models.specialty import Specialty


class Command(BaseCommand):
    help = "Seeder of the database. Doctor table is filled with data."
    DOCTORS = [
        {
            "first_name": "Ana",
            "last_name": "Martínez",
            "username": "anamartinez",
            "email": "ana.martinez@vitalia.com",
            "phone": "666555445",
            "city_id": 3,
            "specialty_id": 7,
            "genre": "Mujer",
            "birth_date": "1985-05-15",
            "identification_number": "87654321B",
            "professional_number": "87654321",
            "price": 60.0,
            "start_schedule": "08:00",
            "end_schedule": "13:00",
            "password": "qwerty"
            },
        {
            "first_name": "Carlos",
            "last_name": "López",
            "username": "carloslopez",
            "email": "carlos.lopez@vitalia.com",
            "phone": "666555446",
            "city_id": 12,
            "specialty_id": 4,
            "genre": "Varon",
            "birth_date": "1979-11-22",
            "identification_number": "12345678C",
            "professional_number": "12345678",
            "price": 70.0,
            "start_schedule": "09:00",
            "end_schedule": "14:00",
            "password": "qwerty"
            },
        {
            "first_name": "María",
            "last_name": "Fernández",
            "username": "mariafernandez",
            "email": "maria.fernandez@vitalia.com",
            "phone": "666555447",
            "city_id": 20,
            "specialty_id": 2,
            "genre": "Mujer",
            "birth_date": "1988-02-15",
            "identification_number": "23456789D",
            "professional_number": "23456789",
            "price": 55.0,
            "start_schedule": "10:00",
            "end_schedule": "15:00",
            "password": "qwerty"
            },
        {
            "first_name": "Luis",
            "last_name": "González",
            "username": "luisgonzalez",
            "email": "luis.gonzalez@vitalia.com",
            "phone": "666555448",
            "city_id": 5,
            "specialty_id": 1,
            "genre": "Varon",
            "birth_date": "1982-03-30",
            "identification_number": "34567890E",
            "professional_number": "34567890",
            "price": 50.0,
            "start_schedule": "08:30",
            "end_schedule": "13:30",
            "password": "qwerty"
            },
        {
            "first_name": "Laura",
            "last_name": "Sánchez",
            "username": "laurasanchez",
            "email": "laura.sanchez@vitalia.com",
            "phone": "666555449",
            "city_id": 18,
            "specialty_id": 9,
            "genre": "Mujer",
            "birth_date": "1991-06-07",
            "identification_number": "45678901F",
            "professional_number": "45678901",
            "price": 65.0,
            "start_schedule": "09:00",
            "end_schedule": "14:00",
            "password": "qwerty"
            },
        {
            "first_name": "Pedro",
            "last_name": "Hernández",
            "username": "pedrohernandez",
            "email": "pedro.hernandez@vitalia.com",
            "phone": "666555450",
            "city_id": 28,
            "specialty_id": 5,
            "genre": "Varon",
            "birth_date": "1985-09-12",
            "identification_number": "56789012G",
            "professional_number": "56789012",
            "price": 60.0,
            "start_schedule": "07:00",
            "end_schedule": "12:00",
            "password": "qwerty"
            },
        {
            "first_name": "Isabel",
            "last_name": "Ruiz",
            "username": "isabelruiz",
            "email": "isabel.ruiz@vitalia.com",
            "phone": "666555451",
            "city_id": 9,
            "specialty_id": 3,
            "genre": "Mujer",
            "birth_date": "1990-10-29",
            "identification_number": "67890123H",
            "professional_number": "67890123",
            "price": 58.0,
            "start_schedule": "08:00",
            "end_schedule": "13:00",
            "password": "qwerty"
            },
        {
            "first_name": "Miguel",
            "last_name": "Moreno",
            "username": "miguelmoreno",
            "email": "miguel.moreno@vitalia.com",
            "phone": "666555452",
            "city_id": 33,
            "specialty_id": 6,
            "genre": "Varon",
            "birth_date": "1986-04-04",
            "identification_number": "78901234I",
            "professional_number": "78901234",
            "price": 52.0,
            "start_schedule": "08:30",
            "end_schedule": "13:30",
            "password": "qwerty"
            },
        {
            "first_name": "Elena",
            "last_name": "García",
            "username": "elenagarcia",
            "email": "elena.garcia@vitalia.com",
            "phone": "666555453",
            "city_id": 15,
            "specialty_id": 8,
            "genre": "Mujer",
            "birth_date": "1992-12-14",
            "identification_number": "89012345J",
            "professional_number": "89012345",
            "price": 50.0,
            "start_schedule": "09:00",
            "end_schedule": "14:00",
            "password": "qwerty"
            },
        {
            "first_name": "Alberto",
            "last_name": "Jiménez",
            "username": "albertojimenez",
            "email": "alberto.jimenez@vitalia.com",
            "phone": "666555454",
            "city_id": 7,
            "specialty_id": 10,
            "genre": "Varon",
            "birth_date": "1983-07-18",
            "identification_number": "90123456K",
            "professional_number": "90123456",
            "price": 48.0,
            "start_schedule": "07:30",
            "end_schedule": "12:30",
            "password": "qwerty"
            }
        ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Creating doctors 🥼')
        for doctor_data in self.DOCTORS:
            try:
                city = City.objects.get(id = doctor_data["city_id"])
                specialty = Specialty.objects.get(id = doctor_data["specialty_id"])
                role = Group.objects.get(name = "Doctor")
                if User.objects.filter(username = doctor_data["username"]).exists():
                    self.stdout.write(self.style.WARNING(f"User {doctor_data['username']} already exists, skipping."))
                    continue

                user = User.objects.create_user(
                        first_name = doctor_data["first_name"],
                        last_name = doctor_data["last_name"],
                        username = doctor_data["username"],
                        email = doctor_data["email"],
                        phone = doctor_data["phone"],
                        city = city,
                        identification_number = doctor_data["identification_number"],
                        genre = doctor_data["genre"],
                        birth_date = doctor_data["birth_date"],
                        password = doctor_data["password"]
                        )
                user.groups.add(role)
                user.save()
                print(f"Doctor {doctor_data['username']} created successfully")

                Doctor.objects.create(
                        user = user,
                        specialty = specialty,
                        professional_number = doctor_data["professional_number"],
                        price = doctor_data["price"],
                        start_schedule = doctor_data["start_schedule"],
                        end_schedule = doctor_data["end_schedule"]
                        )
                print(f"Doctor {doctor_data['first_name']} {doctor_data['last_name']} created successfully")

            except City.DoesNotExist:
                print(f"City with ID {doctor_data['city_id']} does not exist")
            except Specialty.DoesNotExist:
                print(f"Specialty with ID {doctor_data['specialty_id']} does not exist")
            except Exception as e:
                print(f"An error occurred: {e}")
        print("Ending doctors creation 👋")