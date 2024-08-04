from rest_framework import serializers

from patients.models.medical_intervention import MedicalIntervention


class MedicalInterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalIntervention
        fields = '__all__'

