from http import HTTPStatus

from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from doctors.choices.status import Status
from doctors.models.appointment_information import AppointmentInformation
from doctors.models.medical_appointment import MedicalAppointment
from doctors.serializers.medical_appointment import MedicalAppointmentCreateSerializer, MedicalAppointmentSerializer


class MedicalAppointmentViewSet(viewsets.ModelViewSet):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer

    @action(detail=False, methods=['post'], url_path = "create-appointment")
    def create_appointment_patient(self, request):
        data = request.data
        patient = request.user.get_profile()

        if not patient:
            return Response(data = "El usuario no es un paciente", status = HTTPStatus.UNAUTHORIZED)

        try:
            doctor = Doctor.objects.get(pk = data['doctor_id'])
        except Doctor.DoesNotExist:
            return Response(data = "El doctor no existe", status = HTTPStatus.NOT_FOUND)

        serializer = MedicalAppointmentCreateSerializer(data = data)
        if not serializer.is_valid():
            return Response(data = serializer.errors, status = HTTPStatus.BAD_REQUEST)

        appointment_exists = self.queryset.filter(
            doctor = doctor,
            patient = patient,
            patient_appointment = data['patient_appointment']
                )
        if appointment_exists:
            return Response(data = "Ya existe una cita en ese horario", status = HTTPStatus.BAD_REQUEST)

        try:
            with transaction.atomic():
                medical_appointment = MedicalAppointment.objects.create(
                    guid=self.__generate_guid(),
                    status=Status.PENDING,
                    patient_appointment=serializer.validated_data['patient_appointment'],
                    patient=patient,
                    doctor=doctor
                )
                AppointmentInformation.objects.create(
                    reason_consultation=serializer.validated_data['reason_consultation'],
                    medical_appointment=medical_appointment
                )
        except Exception as e:
            return Response(data=str(e), status=HTTPStatus.INTERNAL_SERVER_ERROR)
        response_serializer = MedicalAppointmentSerializer(medical_appointment)
        return Response(data=response_serializer.data, status=HTTPStatus.CREATED)

    def __generate_guid(self):
        prefix = "VIT"
        last_appointment = MedicalAppointment.objects.filter(guid__startswith = prefix).order_by('-created_at').first()
        last_number = int(last_appointment.guid[len(prefix):]) if last_appointment else 0
        new_number = last_number + 1
        return f"{prefix}{str(new_number).zfill(5)}"