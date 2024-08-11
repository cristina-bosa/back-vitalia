from rest_framework import viewsets

from patients.models.medical_history import MedicalHistory
from patients.serializers.medical_history import MedicalHistorySerializer


class MedicalHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalHistorySerializer
    queryset = MedicalHistory.objects.all()
