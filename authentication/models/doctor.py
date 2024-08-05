from django.db import models


from authentication.models.user import User
from doctors.models.city import City
from doctors.models.specialty import Specialty


class Doctor (models.Model):
    professional_number = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_schedule = models.TimeField()
    end_schedule = models.TimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    specialty = models.OneToOneField(Specialty, on_delete=models.CASCADE, related_name='specialty')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    class Meta:
        ordering = ['specialty']
        indexes = [models.Index(fields=['specialty', 'city'])]
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

