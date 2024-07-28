from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.choices.genre import Genre


class User(AbstractUser):
    phone = models.CharField(max_length = 20)
    genre = models.CharField(choices = Genre.choices, max_length = 10)
    birth_date = models.DateField()

