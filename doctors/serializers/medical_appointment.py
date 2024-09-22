from rest_framework import serializers

from authentication.models.doctor import Doctor
from authentication.serializers.patient import PatientAppointmentSerializer, PatientSerializer
from doctors.models.appointment_information import AppointmentInformation
from doctors.models.medical_appointment import MedicalAppointment
from doctors.serializers.appointment_information import AppointmentInformationForMedicalAppointmentSerializer,\
    AppointmentInformationSerializer
from doctors.serializers.doctor import DoctorSerializer


class MedicalAppointmentSerializer(serializers.ModelSerializer):
    appointment_information = AppointmentInformationSerializer(read_only=True)
    class Meta:
        model = MedicalAppointment
        fields = '__all__'


class MedicalAppointmentCreateSerializer(serializers.ModelSerializer):
    reason_consultation = serializers.CharField(required=False, allow_blank=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), source='doctor.id')

    class Meta:
        model = MedicalAppointment
        fields = ['guid', 'status', 'patient_appointment', 'reason_consultation', 'doctor_id']


class MedicalAppointmentDashboardSerializer(serializers.ModelSerializer):
    patient_appointment = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    patient_name = serializers.StringRelatedField(source='patient.user.first_name', read_only=True)
    patient_last_name = serializers.StringRelatedField(source = 'patient.user.last_name', read_only = True)
    reason_consultation = serializers.StringRelatedField(read_only = True)
    doctor = DoctorSerializer()
    class Meta:
        model = MedicalAppointment
        fields = ['id','guid', 'status', 'patient_appointment', 'patient_name','patient_last_name', 'reason_consultation', 'doctor']


class MedicalAppointmentDataSerializer(serializers.ModelSerializer):
    appointment_information = AppointmentInformationForMedicalAppointmentSerializer(read_only=True)
    patient = PatientAppointmentSerializer()
    doctor = DoctorSerializer()
    class Meta:
        model = MedicalAppointment
        fields = '__all__'

class MedicalAppointmentHistoryDataSerializer(serializers.ModelSerializer):
    doctor_name = serializers.StringRelatedField(source='doctor.user.first_name', read_only=True)
    doctor_last_name = serializers.StringRelatedField(source='doctor.user.last_name', read_only=True)
    patient_name = serializers.StringRelatedField(source='patient.user.first_name', read_only=True)
    patient_last_name = serializers.StringRelatedField(source='patient.user.last_name', read_only=True)
    specialty = serializers.StringRelatedField(source='doctor.specialty.name', read_only=True)
    status = serializers.StringRelatedField()
    patient_appointment = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = MedicalAppointment
        fields = ['id', 'guid', 'doctor_name', 'doctor_last_name', 'patient_name', 'patient_last_name', 'specialty',
                  'status', 'patient_appointment']