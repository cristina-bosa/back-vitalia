from rest_framework import viewsets

from patients.models.current_medication import CurrentMedication
from patients.serializers.current_medication import CurrentMedicationlSelectSerializer


class CurrentMedicationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CurrentMedicationlSelectSerializer
    queryset = CurrentMedication.objects.all()

