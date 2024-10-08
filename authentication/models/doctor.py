from django.db import models

from authentication.choices.statusdoctor import StatusDoctor
from authentication.models.user import User
from doctors.models.specialty import Specialty

class Doctor (models.Model):
    professional_number = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_schedule = models.TimeField()
    end_schedule = models.TimeField()
    status = models.CharField(choices = StatusDoctor.choices, max_length = 20, default = StatusDoctor.PENDING, blank = True)
    stars = models.DecimalField(max_digits=2, decimal_places=1, default=0, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='specialty')


    class Meta:
        ordering = ['-stars']
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'