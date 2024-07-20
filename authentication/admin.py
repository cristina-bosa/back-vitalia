from django.contrib import admin

from authentication.models import User
from authentication.models.doctor import Doctor
from authentication.models.patient import Patient

# Register your models here.
admin.site.register({
    User,
    Doctor,
    Patient
    })
