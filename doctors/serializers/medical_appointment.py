from rest_framework import serializers

from authentication.models.doctor import Doctor
from doctors.models.appointment_information import AppointmentInformation
from doctors.models.medical_appointment import MedicalAppointment
from doctors.serializers.appointment_information import AppointmentInformationSerializer


class MedicalAppointmentSerializer(serializers.ModelSerializer):
    appointment_information = AppointmentInformationSerializer(many=True, read_only=True)
    class Meta:
        model = MedicalAppointment
        fields = '__all__'


class MedicalAppointmentCreateSerializer(serializers.ModelSerializer):
    reason_consultation = serializers.CharField(required=False, allow_blank=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), source='doctor.id')

    class Meta:
        model = MedicalAppointment
        fields = ['guid', 'status', 'patient_appointment', 'reason_consultation', 'doctor_id']