from django.db import models

from authentication.models.doctor import Doctor
from authentication.models.patient import Patient


class Review (models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank = True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['doctor']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
