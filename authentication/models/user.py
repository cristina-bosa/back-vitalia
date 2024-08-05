from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.choices.genre import Genre


class User(AbstractUser):
    birth_date = models.DateField()
    genre = models.CharField(choices = Genre.choices, max_length = 10)
    phone = models.CharField(max_length = 20)
    identification_number = models.CharField(max_length = 20, unique=True)

    def is_doctor(self):
        return hasattr(self, 'doctor')

    def is_patient(self):
        return hasattr(self, 'patient')

    def is_admin(self):
        return self.is_staff

    def get_profile(self):
        if self.is_doctor():
            return self.doctor
        elif self.is_patient():
            return self.patient
        return None