from django.db import models

from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from doctors.choices.status import Status


class MedicalAppointment(models.Model):
    guid = models.CharField(max_length=100, unique=True, blank=True)
    status = models.CharField(choices = Status.choices, max_length = 20, default = Status.PENDING, blank = True)
    patient_appointment = models.DateTimeField() # cuando el paciente solicita la cita
    start_appointment = models.DateTimeField(blank = True, null = True) # cuando el doctor inicia la cita
    end_appointment = models.DateTimeField(blank = True, null = True) # cuando el doctor finaliza la consulta
    accepted_at = models.DateTimeField(blank = True, null = True)  # cuando el doctor acepta la cita
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank = True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # cuando se crea la cita
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-patient_appointment']
        verbose_name = 'Medical Appointment'
        verbose_name_plural = 'Medical Appointments'

    @property
    def reason_consultation(self):
        return self.appointment_information.first().reason_consultation
