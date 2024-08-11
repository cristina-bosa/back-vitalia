from rest_framework import viewsets


from patients.models.medical_intervention import MedicalIntervention
from patients.serializers.medical_intervention import MedicalInterventionSerializer


class MedicalInterventionViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalInterventionSerializer
    queryset = MedicalIntervention.objects.all()
