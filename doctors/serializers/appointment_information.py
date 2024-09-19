from rest_framework import serializers

from doctors.models.appointment_information import AppointmentInformation


class AppointmentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentInformation
        fields = '__all__'


class AppointmentInformationForMedicalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentInformation
        fields = ['id', 'reason_consultation','symptoms', 'diagnosis', 'medications', 'treatment','recommendations']
