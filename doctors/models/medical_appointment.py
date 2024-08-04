from django.db import models

from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from doctors.choices.status import Status


class MedicalAppointment(models.Model):
    guid = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices = Status.choices, max_length = 20)
    patient_appointment = models.DateTimeField() # cuando el paciente solicita la cita
    start_appointment = models.DateTimeField() # cuando el doctor inicia la cita
    end_appointment = models.DateTimeField() # cuando el doctor finaliza la consulta
    accepted_at = models.DateTimeField()  # cuando el doctor acepta la cita
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # cuando se crea la cita
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Medical Appointment'
        verbose_name_plural = 'Medical Appointments'
