from django.db import models

from authentication.models.user import User
from patients.models.medical_history import MedicalHistory


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_history = models.OneToOneField(MedicalHistory, on_delete = models.CASCADE, related_name = 'medical_history')

    class Meta:
        ordering = ['user']
        verbose_name = 'patient'
        verbose_name_plural = 'patients'

