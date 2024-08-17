from django.db import models


class RelevantDiseases(models.Model):
    name = models.CharField(max_length = 100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'relevant_disease'
        verbose_name_plural = 'relevant_diseases'

    def __str__(self):
        return self.name