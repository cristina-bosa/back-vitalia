from rest_framework import serializers

from authentication.models.patient import Patient
from authentication.serializers.user import UserProfileSerializer


class PatientSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Patient
        fields = 'user', 'medical_history'