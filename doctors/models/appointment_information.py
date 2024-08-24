from django.db import models

from doctors.models.medical_appointment import MedicalAppointment


class AppointmentInformation(models.Model):
    reason_consultation = models.TextField()
    symptoms = models.TextField(blank=True, null = True)
    diagnosis = models.TextField(blank=True, null = True)
    medications = models.TextField(blank=True, null = True)
    treatment = models.TextField(blank=True, null = True)
    recommendations = models.TextField(blank=True, null = True)
    medical_appointment = models.ForeignKey(MedicalAppointment, on_delete=models.CASCADE,
                                            related_name='appointment_information', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)


