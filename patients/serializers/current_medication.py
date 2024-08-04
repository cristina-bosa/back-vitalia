from rest_framework import serializers

from patients.models.current_medication import CurrentMedication


class CurrentMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMedication
        fields = '__all__'

