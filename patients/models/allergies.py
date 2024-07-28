from django.db import models


class Allergies (models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Allergy'
        verbose_name_plural = 'Allergies'