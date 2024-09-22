from django.db import models
from django.db.models import ManyToManyField

from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases


class MedicalHistory(models.Model):
    allergies = ManyToManyField(Allergies, related_name = 'allergies', blank=True)
    relevant_diseases = ManyToManyField(RelevantDiseases, related_name = 'relevant_diseases', blank=True)
    current_medication = ManyToManyField(CurrentMedication, related_name = 'current_medication', blank=True)
    medical_intervention = ManyToManyField(MedicalIntervention, related_name = 'medical_intervention', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'medical_history'
        verbose_name_plural = 'medical_histories'

