from django.db import models


class RelevantDiseases(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        ordering = ['name']
        verbose_name = 'relevant_disease'
        verbose_name_plural = 'relevant_diseases'
