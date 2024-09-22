from rest_framework import serializers

from patients.models.medical_intervention import MedicalIntervention


class MedicalInterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalIntervention
        fields = '__all__'


class MedicalInterventionSelectSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = MedicalIntervention
        fields = ['value','label']