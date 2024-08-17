from django.core.management import BaseCommand, CommandError

from doctors.models.city import City
from doctors.models.specialty import Specialty
from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_history import MedicalHistory
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases


class Command(BaseCommand):
    help = "Seeder of the database. Reference tables are filled with data."
    SPECIALTIES = ["Cardiología", "Dermatología", "Neurología", "Pediatría", "Ginecología", "Oncología", "Psiquiatría", "Oftalmología", "Cirugía General", "Ortopedia"]
    ALLERGIES = ["Polen", "Ácaros", "Alimentos", "Medicamentos", "Picadura de insectos", "Moho", "Látex", "Animales", "Perfumes", "Níquel"]
    RELEVANT_DISEASESS = ["Diabetes", "Hipertensión", "Asma", "Artritis", "Cáncer", "Enfermedad de Alzheimer", "Gripe", "Depresión", "Migraña", "Enfermedad cardíaca"]
    CURRENT_MEDICATIONS = ["Ibuprofeno", "Paracetamol", "Amoxicilina", "Metformina", "Loratadina", "Omeprazol", "Atorvastatina", "Lisinopril", "Diazepam", "Aspirina"]
    MEDICAL_INTERVENTIONS = ["Apendicectomía", "Colecistectomía", "Bypass gástrico", "Angioplastia", "Cesárea", "Reemplazo de rodilla", "Resección de tumor", "Cateterismo cardíaco", "Lobectomía", "Endoscopia"]


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("\nCreating specialties 👨‍⚕️")
        for specialty in self.SPECIALTIES:
            try:
                Specialty.objects.create(name=specialty)
                print(f"{specialty} created")
            except Exception as e:
                pass
        print("Ending specialties creation👋")
        print("\nCreating allergies ☘️")
        for allergy in self.ALLERGIES:
            try:
                Allergies.objects.create(name=allergy)
                print(f"{allergy} created")
            except Exception as e:
                pass
        print("Ending allergies creation👋")
        print("\nCreating relevant diseases 💉")
        for relevant_disease in self.RELEVANT_DISEASESS:
            try:
                RelevantDiseases.objects.create(name=relevant_disease)
                print(f"{relevant_disease} created")
            except Exception as e:
                pass
        print("Ending relevant diseases creation👋")
        print("\nCreating current medications 💊")
        for current_medication in self.CURRENT_MEDICATIONS:
            try:
                CurrentMedication.objects.create(name=current_medication)
                print(f"{current_medication} created")
            except Exception as e:
                pass
        print("Ending current medications creation👋")
        print("\nCreating medical interventions ❤️‍🩹")
        for medical_intervention in self.MEDICAL_INTERVENTIONS:
            try:
                MedicalIntervention.objects.create(name=medical_intervention)
                print(f"{medical_intervention} created")
            except Exception as e:
                pass
        print("Ending medical interventios creation👋")