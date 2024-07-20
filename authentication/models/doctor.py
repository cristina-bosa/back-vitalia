from django.db import models

from authentication.choices.speciality import Speciality
from authentication.models.user import User


class Doctor (models.Model):
    specialty = models.CharField(choices = Speciality.choices, max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['specialty']
        indexes = [models.Index(fields=['specialty'])]
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

