from rest_framework import serializers

from patients.models.medical_history import MedicalHistory


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

