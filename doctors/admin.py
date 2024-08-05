from django.contrib import admin

from doctors.models.appointment_information import AppointmentInformation
from doctors.models.city import City
from doctors.models.medical_appointment import MedicalAppointment
from doctors.models.medical_attachment import MedicalAttachment
from doctors.models.review import Review
from doctors.models.specialty import Specialty

# Register your models here.
admin.site.register({
    AppointmentInformation,
    City,
    MedicalAppointment,
    MedicalAttachment,
    Review,
    Specialty
    })