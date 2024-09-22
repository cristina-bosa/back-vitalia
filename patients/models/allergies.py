from django.db import models


class Allergies (models.Model):
    name = models.CharField(max_length = 100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'allergy'
        verbose_name_plural = 'allergies'

    def __str__(self):
        return self.name