from http import HTTPStatus

from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models.doctor import Doctor
from authentication.permissions.groups import IsUserDoctor, IsUserPatient
from authentication.permissions.medical_appointment import IsMedicalAppointmentConfirmed,\
    IsMedicalAppointmentInProgress, IsMedicalAppointmentPending,\
    IsMedicalAppointmentPendingOrConfirmed

from doctors.choices.status import Status
from doctors.models.appointment_information import AppointmentInformation
from doctors.models.medical_appointment import MedicalAppointment
from doctors.serializers.medical_appointment import MedicalAppointmentCreateSerializer,\
    MedicalAppointmentDashboardSerializer, MedicalAppointmentPatientDataSerializer, MedicalAppointmentSerializer


class MedicalAppointmentViewSet(viewsets.ModelViewSet):
    queryset = MedicalAppointment.objects.filter(status__in = [Status.PENDING, Status.CONFIRMED, Status.IN_PROGRESS])
    serializer_class = MedicalAppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_patient():
            return MedicalAppointment.objects.filter(patient = user.get_profile())
        elif user.is_doctor():
            return MedicalAppointment.objects.filter(doctor = user.get_profile())
        return MedicalAppointment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MedicalAppointmentPatientDataSerializer(instance)
        return Response(serializer.data)

    @action(detail = False, methods = ['post'], url_path = "book",
            permission_classes = [IsAuthenticated, IsUserPatient])
    def book(self, request):
        data = request.data
        patient = request.user.get_profile()

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
            return Response(data = "Ya existe una cita en ese horario", status = HTTPStatus.NOT_ACCEPTABLE)

        try:
            with transaction.atomic():
                medical_appointment = MedicalAppointment.objects.create(
                        guid = self.__generate_guid(),
                        status = Status.PENDING,
                        patient_appointment = serializer.validated_data['patient_appointment'],
                        patient = patient,
                        doctor = doctor
                        )
                AppointmentInformation.objects.create(
                        reason_consultation = serializer.validated_data['reason_consultation'],
                        medical_appointment = medical_appointment
                        )
        except Exception as e:
            return Response(data = str(e), status = HTTPStatus.INTERNAL_SERVER_ERROR)
        response_serializer = MedicalAppointmentSerializer(medical_appointment)
        return Response(data = response_serializer.data, status = HTTPStatus.CREATED)

    def __generate_guid(self):
        prefix = "VIT"
        last_appointment = MedicalAppointment.objects.filter(guid__startswith = prefix).order_by('-created_at').first()
        last_number = int(last_appointment.guid[len(prefix):]) if last_appointment else 0
        new_number = last_number + 1
        return f"{prefix}{str(new_number).zfill(5)}"

    @action(detail = True, methods = ['post'], url_path = "unbook",
            permission_classes = [IsAuthenticated, IsMedicalAppointmentPendingOrConfirmed])
    def unbook(self, request):
        medical_appointment = self.get_object()
        medical_appointment.status = Status.CANCELED
        medical_appointment.save()
        return Response(data = MedicalAppointmentSerializer(medical_appointment).data, status = HTTPStatus.OK)

    @action(detail = False, methods = ['get'], url_path = "(?P<doctor_action>("
                                                          "pending|confirmed|in-progress|canceled|finished))",
            permission_classes = [IsAuthenticated, IsUserDoctor])
    def get_medical_appointment(self, request, *args, **kwargs, ):
        doctor_action = kwargs.get('doctor_action')
        appointments = []
        match doctor_action:
            case "pending":
                appointments = self.get_queryset().filter(status = Status.PENDING)
            case "confirmed":
                appointments = self.get_queryset().filter(status = Status.CONFIRMED)
            case "in-progress":
                appointments = self.get_queryset().filter(status = Status.IN_PROGRESS)
            case "canceled":
                appointments = self.get_queryset().filter(status = Status.CANCELED)
            case "finished":
                appointments = self.get_queryset().filter(status = Status.FINISHED)
            case _:
                appointments = self.get_queryset()
        data = MedicalAppointmentDashboardSerializer(appointments, many = True).data
        return Response(data = data, status = HTTPStatus.OK)

    @action(detail = False, methods = ['post'], url_path = "filter/(?P<doctor_action>("
                                                          "pending|confirmed|in-progress|canceled|finished))",
            permission_classes = [IsAuthenticated, IsUserDoctor])
    def get_medical_appointment_by_date(self, request, *args, **kwargs, ):
        doctor_action = kwargs.get('doctor_action')
        start_date = request.data.get('start_date')
        if not start_date:
            return Response(data = {"message": "Field start_date is required"}, status = HTTPStatus.BAD_REQUEST)
        end_date = request.data.get('end_date', None)
        match doctor_action:
            case "pending":
                appointments = self.get_queryset().filter(status = Status.PENDING)
            case "confirmed":
                appointments = self.get_queryset().filter(status = Status.CONFIRMED)
            case "in-progress":
                appointments = self.get_queryset().filter(status = Status.IN_PROGRESS)
            case "canceled":
                appointments = self.get_queryset().filter(status = Status.CANCELED)
            case "finished":
                appointments = self.get_queryset().filter(status = Status.FINISHED)
            case _:
                appointments = self.get_queryset()
        appointments = appointments.filter(patient_appointment__gte = start_date)
        if end_date:
            appointments = appointments.filter(patient_appointment__lte = end_date)
        data = MedicalAppointmentDashboardSerializer(appointments, many = True).data
        return Response(data = data, status = HTTPStatus.OK)

    @action(detail = True, methods = ['post'], url_path = "(accept|reject)",
            permission_classes = [IsAuthenticated, IsUserDoctor, IsMedicalAppointmentPending])
    def manage_pending_appointment(self, request, pk):
        medical_appointment = self.get_object()
        if request.path.endswith("accept"):
            medical_appointment.status = Status.CONFIRMED
        else:
            medical_appointment.status = Status.CANCELED
        medical_appointment.save()
        return Response(data = MedicalAppointmentSerializer(medical_appointment).data, status = HTTPStatus.OK)

    @action(detail = True, methods = ['post'], url_path = "start-appointment",
            permission_classes = [IsAuthenticated, IsUserDoctor, IsMedicalAppointmentConfirmed])
    def start_appointment(self, request):
        medical_appointment = self.get_object()
        medical_appointment.status = Status.IN_PROGRESS
        medical_appointment.save()
        return Response(data = MedicalAppointmentSerializer(medical_appointment).data, status = HTTPStatus.OK)

    @action(detail = True, methods = ['post'], url_path = "finish-appointment",
            permission_classes = [IsAuthenticated, IsUserDoctor, IsMedicalAppointmentInProgress])
    def finish_appointment(self, request):
        medical_appointment = self.get_object()
        medical_appointment.status = Status.FINISHED
        medical_appointment.save()
        return Response(data = MedicalAppointmentSerializer(medical_appointment).data, status = HTTPStatus.OK)

    @action(detail = True, methods = ['post'], url_path = "appointment-information",
            permission_classes = [IsAuthenticated, IsUserDoctor, IsMedicalAppointmentInProgress])
    def update_appointment_information(self, request):
        #TODO: introducir la informacion del informe medico
        medical_appointment = self.get_object()
        # data = request.data
        # appointment_information = medical_appointment.appointment_information
        # appointment_information.reason_consultation = data.get('reason_consultation', appointment_information.reason_consultation)
        # appointment_information.save()
        return Response(data = MedicalAppointmentSerializer(medical_appointment).data, status = HTTPStatus.OK)
