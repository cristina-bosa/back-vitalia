from rest_framework import serializers

from patients.models.medical_history import MedicalHistory


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = 'id', 'allergies', 'current_medication', 'medical_intervention', 'relevant_diseases'

class MedicalHistoryGetSerializer(serializers.ModelSerializer):
    allergies = serializers.StringRelatedField(many = True)
    current_medication = serializers.StringRelatedField(many = True)
    medical_intervention = serializers.StringRelatedField(many = True)
    relevant_diseases = serializers.StringRelatedField(many = True)
    class Meta:
        model = MedicalHistory
        fields = 'id', 'allergies', 'current_medication', 'medical_intervention', 'relevant_diseases'

