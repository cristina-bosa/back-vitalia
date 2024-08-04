from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.choices.genre import Genre


class User(AbstractUser):
    birth_date = models.DateField()
    genre = models.CharField(choices = Genre.choices, max_length = 10)
    phone = models.CharField(max_length = 20)
    identification_number = models.CharField(max_length = 20)

