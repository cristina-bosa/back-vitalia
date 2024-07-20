from django.db import models

from authentication.choices.genre import Genre
from authentication.models.user import User


class Patient(models.Model):
    birth_date = models.DateField()
    genre = models.CharField(choices = Genre.choices, max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['genre']
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

