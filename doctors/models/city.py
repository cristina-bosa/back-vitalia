from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
