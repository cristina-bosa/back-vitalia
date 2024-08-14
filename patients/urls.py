from rest_framework import routers

from patients.views.allergies import AllergiesViewSet
from patients.views.current_medication import CurrentMedicationViewSet
from patients.views.medical_history import MedicalHistoryViewSet
from patients.views.medical_intervention import MedicalInterventionViewSet
from patients.views.relevant_diseases import RelevantDiseasesViewSet

router = routers.DefaultRouter()
router.register('allergies', AllergiesViewSet, basename = 'allergies')
router.register('current-medication', CurrentMedicationViewSet, basename = 'current-medication')
router.register('medical-history', MedicalHistoryViewSet, basename = 'medical-history')
router.register('medical-intervention', MedicalInterventionViewSet, basename = 'medical-intervention')
router.register('relevant-diseases', RelevantDiseasesViewSet, basename = 'relevant-diseases')
router.urlpatterns = router.urls
