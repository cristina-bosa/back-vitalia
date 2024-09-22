from django.db import models


class Status(models.TextChoices):
    PENDING = 'Pendiente'
    CONFIRMED = 'Confirmada'
    IN_PROGRESS = 'En progreso'
    CANCELED = 'Cancelada'
    FINISHED = 'Finalizada'

