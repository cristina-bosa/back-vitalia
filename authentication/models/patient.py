from django.db import models

from authentication.choices.genre import Genre
from authentication.models.user import User


class Patient(models.Model):
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['birth_date']
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

