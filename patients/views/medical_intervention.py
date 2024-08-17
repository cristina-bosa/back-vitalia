from rest_framework import viewsets


from patients.models.medical_intervention import MedicalIntervention
from patients.serializers.medical_intervention import MedicalInterventionSelectSerializer


class MedicalInterventionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedicalInterventionSelectSerializer
    queryset = MedicalIntervention.objects.all()
