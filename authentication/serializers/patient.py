from rest_framework import serializers

from authentication.models.patient import Patient
from authentication.serializers.user import UserProfileSerializer
from patients.serializers.medical_history import MedicalHistoryGetSerializer


class PatientSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    medical_history = MedicalHistoryGetSerializer()
    class Meta:
        model = Patient
        fields = 'user', 'medical_history'
