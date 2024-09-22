from rest_framework import routers

from doctors.views.doctor import DoctorViewSet
from doctors.views.history import HistoryViewSet
from doctors.views.medical_appointment import MedicalAppointmentViewSet

router = routers.DefaultRouter()
router.register('history', HistoryViewSet, basename = 'history')
router.register('medical-appointment', MedicalAppointmentViewSet, basename = 'medical-appointment')
router.register('', DoctorViewSet, basename = 'doctor')

router.urlpatterns = router.urls
