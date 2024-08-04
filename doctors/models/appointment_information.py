from django.db import models

from doctors.models.medical_appointment import MedicalAppointment


class AppointmentInformation(models.Model):
    reason_consultation = models.TextField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    medications = models.TextField()
    treatment = models.TextField()
    recommendations = models.TextField()
    medical_appointment = models.ForeignKey(MedicalAppointment, on_delete=models.CASCADE, related_name='appointment_information')
    created_at = models.DateTimeField(auto_now_add=True)

