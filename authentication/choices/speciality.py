from django.db import models


class Speciality(models.TextChoices):
    GENERAL_MEDICINE = 'Medicina general'
    PEDIATRICS = 'Pediatría'
    CARDIOLOGY = 'Cardilogía'
    DERMATOLOGY = 'Dermatología'
    GYNECOLOGY = 'Ginecología'
    OPHTHALMOLOGY = 'Oftalmología'
    OTORHINOLARYNGOLOGY = 'Otorrinolaringología'
    PSYCHIATRY = 'Psiquiatría'
    UROLOGY = 'Urología'
    NEUROLOGY = 'Neurología'
    ORTHOPEDICS = 'Ortopedia'
    TRAUMATOLOGY = 'Traumatología'
    ENDOCRINOLOGY = 'Endocrinología'
    ONCOLOGY = 'Oncología'
    NUTRITION = 'Nutricionista'
    DENTISTRY = 'Dentista'
    PHYSIOTHERAPY = 'Fisioterapia'
    PSYCHOLOGY = 'Psicología'
    NURSING = 'Enfermería'
