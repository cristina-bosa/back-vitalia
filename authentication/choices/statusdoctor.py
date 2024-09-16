from django.db import models


class StatusDoctor(models.TextChoices):
    PENDING = 'Pendiente'
    CONFIRMED = 'Confirmado'
    CANCELED = 'Cancelado'
