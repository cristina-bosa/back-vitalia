from rest_framework import serializers

from authentication.models.patient import Patient
from authentication.serializers.user import PatientProfileSerializer


class PatientSerializer(serializers.ModelSerializer):
    user = PatientProfileSerializer()
    class Meta:
        model = Patient
        fields = 'user', 'medical_history'