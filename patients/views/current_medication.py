from rest_framework import viewsets

from patients.models.current_medication import CurrentMedication
from patients.serializers.current_medication import CurrentMedicationSerializer


class CurrentMedicationViewSet(viewsets.ModelViewSet):
    serializer_class = CurrentMedicationSerializer
    queryset = CurrentMedication.objects.all()

