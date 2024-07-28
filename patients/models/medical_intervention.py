from django.db import models


class MedicalIntervention(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'medical_intervention'
        verbose_name_plural = 'medical_interventiones'

