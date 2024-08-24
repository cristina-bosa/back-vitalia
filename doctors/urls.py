from rest_framework import routers

from doctors.views.doctor import DoctorViewSet
from doctors.views.medical_appointment import MedicalAppointmentViewSet

router = routers.DefaultRouter()
router.register('medical-appoinments', MedicalAppointmentViewSet, basename = 'medical_appoinments')
router.register('', DoctorViewSet, basename = 'doctor')

router.urlpatterns = router.urls
