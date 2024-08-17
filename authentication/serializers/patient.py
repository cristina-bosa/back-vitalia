from rest_framework import serializers

from authentication.models.patient import Patient
from authentication.serializers.user import UserProfileSerializer
from patients.serializers.medical_history import MedicalHistorySerializer


class PatientSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    medical_history = MedicalHistorySerializer()
    class Meta:
        model = Patient
        fields = 'user', 'medical_history'
