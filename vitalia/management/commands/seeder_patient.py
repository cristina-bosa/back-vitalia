from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from authentication.models.patient import Patient
from authentication.models.user import User
from doctors.models.city import City
from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_history import MedicalHistory
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases


class Command(BaseCommand):
    help = "Seeder of the database. Patient table is filled with data."
    PATIENTS = [
        {
            "first_name": "Albert",
            "last_name": "Johnson",
            "username": "albertjohnson",
            "password": "qwerty123",
            "email": "albert.johnson@vitalia.com",
            "phone": "666555454",
            "city_id": 7,
            "genre": "Male",
            "birth_date": "1983-07-18",
            "identification_number": "90123456K",
            "medical_history": {
                "allergies": [1, 6],
                "relevant_diseases": [3],
                "current_medication": [2, 7],
                "medical_intervention": [1]
                }
            },
        {
            "first_name": "Mary",
            "last_name": "Smith",
            "username": "marysmith",
            "password": "securepass1",
            "email": "mary.smith@vitalia.com",
            "phone": "666555455",
            "city_id": 12,
            "genre": "Female",
            "birth_date": "1990-05-12",
            "identification_number": "81234567M",
            "medical_history": {
                "allergies": [2, 4],
                "relevant_diseases": [5, 9],
                "current_medication": [4],
                "medical_intervention": [2, 8]
                }
            },
        {
            "first_name": "Charles",
            "last_name": "Williams",
            "username": "charleswilliams",
            "password": "mypassword2",
            "email": "charles.williams@vitalia.com",
            "phone": "666555456",
            "city_id": 20,
            "genre": "Male",
            "birth_date": "1975-11-23",
            "identification_number": "71234567L",
            "medical_history": {
                "allergies": [3],
                "relevant_diseases": [7],
                "current_medication": [3, 6],
                "medical_intervention": [1, 9]
                }
            },
        {
            "first_name": "Laura",
            "last_name": "Brown",
            "username": "laurabrown",
            "password": "password123",
            "email": "laura.brown@vitalia.com",
            "phone": "666555457",
            "city_id": 3,
            "genre": "Female",
            "birth_date": "1988-04-04",
            "identification_number": "61234567J",
            "medical_history": {
                "allergies": [1, 7],
                "relevant_diseases": [4],
                "current_medication": [2, 8],
                "medical_intervention": [3]
                }
            },
        {
            "first_name": "Peter",
            "last_name": "Davis",
            "username": "peterdavis",
            "password": "securepass2",
            "email": "peter.davis@vitalia.com",
            "phone": "666555458",
            "city_id": 5,
            "genre": "Male",
            "birth_date": "1982-01-01",
            "identification_number": "51234567G",
            "medical_history": {
                "allergies": [5, 8],
                "relevant_diseases": [2],
                "current_medication": [1],
                "medical_intervention": [4, 6]
                }
            },
        {
            "first_name": "Helen",
            "last_name": "Miller",
            "username": "helenmiller",
            "password": "password456",
            "email": "helen.miller@vitalia.com",
            "phone": "666555459",
            "city_id": 9,
            "genre": "Female",
            "birth_date": "1992-12-14",
            "identification_number": "51234568H",
            "medical_history": {
                "allergies": [3, 9],
                "relevant_diseases": [8],
                "current_medication": [5],
                "medical_intervention": [2]
                }
            },
        {
            "first_name": "James",
            "last_name": "Wilson",
            "username": "jameswilson",
            "password": "mypassword3",
            "email": "james.wilson@vitalia.com",
            "phone": "666555460",
            "city_id": 15,
            "genre": "Male",
            "birth_date": "1995-08-09",
            "identification_number": "31234567F",
            "medical_history": {
                "allergies": [1],
                "relevant_diseases": [5, 6],
                "current_medication": [6],
                "medical_intervention": [5]
                }
            },
        {
            "first_name": "Anna",
            "last_name": "Moore",
            "username": "annamoore",
            "password": "securepass3",
            "email": "anna.moore@vitalia.com",
            "phone": "666555461",
            "city_id": 18,
            "genre": "Female",
            "birth_date": "1985-06-30",
            "identification_number": "91234567D",
            "medical_history": {
                "allergies": [4, 10],
                "relevant_diseases": [9, 10],
                "current_medication": [4, 7],
                "medical_intervention": [3, 8]
                }
            },
        {
            "first_name": "Isabella",
            "last_name": "Taylor",
            "username": "isabellataylor",
            "password": "password789",
            "email": "isabella.taylor@vitalia.com",
            "phone": "666555462",
            "city_id": 22,
            "genre": "Female",
            "birth_date": "1991-03-11",
            "identification_number": "11234567A",
            "medical_history": {
                "allergies": [7],
                "relevant_diseases": [2, 4],
                "current_medication": [3],
                "medical_intervention": [1, 10]
                }
            },
        {
            "first_name": "Michael",
            "last_name": "Anderson",
            "username": "michaelanderson",
            "password": "securepass4",
            "email": "michael.anderson@vitalia.com",
            "phone": "666555463",
            "city_id": 25,
            "genre": "Male",
            "birth_date": "1986-09-15",
            "identification_number": "21234567E",
            "medical_history": {
                "allergies": [2, 5],
                "relevant_diseases": [1, 7],
                "current_medication": [2],
                "medical_intervention": [4]
                }
            },
        {
            "first_name": "Emily",
            "last_name": "Thomas",
            "username": "emilythomas",
            "password": "password101",
            "email": "emily.thomas@vitalia.com",
            "phone": "666555464",
            "city_id": 30,
            "genre": "Female",
            "birth_date": "1989-11-22",
            "identification_number": "32145678E",
            "medical_history": {
                "allergies": [6],
                "relevant_diseases": [3, 5],
                "current_medication": [8],
                "medical_intervention": [2, 7]
                }
            },
        {
            "first_name": "Daniel",
            "last_name": "Jackson",
            "username": "danieljackson",
            "password": "mypassword4",
            "email": "daniel.jackson@vitalia.com",
            "phone": "666555465",
            "city_id": 35,
            "genre": "Male",
            "birth_date": "1978-02-15",
            "identification_number": "12345678D",
            "medical_history": {
                "allergies": [8, 10],
                "relevant_diseases": [2, 6],
                "current_medication": [1],
                "medical_intervention": [3]
                }
            }
        ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Creating patients 🙍‍♀️')
        for patient_data in self.PATIENTS:
            try:
                city = City.objects.get(id = patient_data["city_id"])
                role = Group.objects.get(name = "Patient")

                if User.objects.filter(username = patient_data["username"]).exists():
                    print(f"User {patient_data['username']} already exists, skipping.")
                    continue

                user = User.objects.create_user(
                        first_name = patient_data["first_name"],
                        last_name = patient_data["last_name"],
                        username = patient_data["username"],
                        email = patient_data["email"],
                        phone = patient_data["phone"],
                        city = city,
                        identification_number = patient_data["identification_number"],
                        genre = patient_data["genre"],
                        birth_date = patient_data["birth_date"],
                        password = patient_data["password"]
                        )
                user.groups.add(role)
                user.save()
                print(f"Patient {patient_data['username']} created successfully")

                medical_history_data = patient_data["medical_history"]
                medical_history = MedicalHistory.objects.create()
                allergies = Allergies.objects.filter(id__in = medical_history_data.get("allergies", []))
                relevant_diseases = RelevantDiseases.objects.filter(id__in = medical_history_data.get(
                        "relevant_diseases", []))
                current_medication = CurrentMedication.objects.filter(
                    id__in = medical_history_data.get("current_medication", []))
                medical_intervention = MedicalIntervention.objects.filter(
                    id__in = medical_history_data.get("medical_intervention", []))

                medical_history.allergies.set(allergies)
                medical_history.relevant_diseases.set(relevant_diseases)
                medical_history.current_medication.set(current_medication)
                medical_history.medical_intervention.set(medical_intervention)

                print(f"Medical history for {patient_data['first_name']} created successfully")
                Patient.objects.create(
                        user = user,
                        medical_history = medical_history
                        )
                print(f"Patient {patient_data['first_name']} {patient_data['last_name']} created successfully")

            except City.DoesNotExist:
                print(f"City with ID {patient_data['city_id']} does not exist")
            except Exception as e:
                print(f"An error occurred: {e}")
        print("Ending patient creation 👋")