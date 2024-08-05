from django.contrib import admin

from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_history import MedicalHistory
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases

# Register your models here.
admin.site.register({
    Allergies,
    CurrentMedication,
    MedicalHistory,
    MedicalIntervention,
    RelevantDiseases
    })
