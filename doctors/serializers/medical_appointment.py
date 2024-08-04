from rest_framework import serializers

from doctors.models.medical_appointment import MedicalAppointment


class MedicalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAppointment
        fields = '__all__'

