from rest_framework import serializers

from patients.models.current_medication import CurrentMedication


class CurrentMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMedication
        fields = '__all__'


class CurrentMedicationlSelectSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = CurrentMedication
        fields = ['value','label']