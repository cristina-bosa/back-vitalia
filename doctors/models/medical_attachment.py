from django.db import models

from authentication.models.doctor import Doctor
from doctors.models.medical_appointment import MedicalAppointment


class MedicalAttachment(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='medical_attachments/')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medical_appointment = models.ForeignKey(MedicalAppointment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Medical Attachment'
        verbose_name_plural = 'Medical Attachments'

    def __str__(self):
        return self.name
