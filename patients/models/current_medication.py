from django.db import models


class CurrentMedication(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'current_medication'
        verbose_name_plural = 'current_medications'