from django.db import models


class Specialty (models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

