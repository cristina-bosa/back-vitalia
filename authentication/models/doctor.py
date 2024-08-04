from django.db import models


from authentication.models.user import User
from doctors.models.city import City
from doctors.models.speciality import Speciality


class Doctor (models.Model):
    professional_number = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.TimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.OneToOneField(Speciality, on_delete=models.CASCADE, related_name='specialty')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    class Meta:
        ordering = ['specialty']
        indexes = [models.Index(fields=['specialty'])]
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

