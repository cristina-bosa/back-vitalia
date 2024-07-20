from django.db import models


class Genre(models.TextChoices):
    MASCULINE = 'Varon'
    FEMININE = 'Mujer'
