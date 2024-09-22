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


class PatientAppointmentSerializer(serializers.ModelSerializer):
    first_name = serializers.StringRelatedField(source = 'user.first_name', read_only = True)
    last_name = serializers.StringRelatedField(source = 'user.last_name', read_only = True)
    genre = serializers.StringRelatedField(source = 'user.genre', read_only = True)
    birth_date = serializers.StringRelatedField(source = 'user.birth_date', read_only = True)
    identification_number = serializers.StringRelatedField(source = 'user.identification_number', read_only = True)
    email = serializers.StringRelatedField(source = 'user.email', read_only = True)
    phone = serializers.StringRelatedField(source = 'user.phone', read_only = True)
    medical_history = MedicalHistoryGetSerializer()
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'genre', 'birth_date', 'identification_number', 'email', 'phone', 'medical_history']