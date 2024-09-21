from rest_framework import viewsets

from doctors.choices.status import Status
from doctors.models.medical_appointment import MedicalAppointment
from doctors.serializers.medical_appointment import MedicalAppointmentDashboardSerializer,\
    MedicalAppointmentHistoryDataSerializer, MedicalAppointmentSerializer


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MedicalAppointment.objects.filter(status__in = [Status.CONFIRMED, Status.IN_PROGRESS, Status.FINISHED])
    serializer_class = MedicalAppointmentHistoryDataSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_patient():
            return MedicalAppointment.objects.filter(patient = user.get_profile())
        elif user.is_doctor():
            return MedicalAppointment.objects.filter(doctor = user.get_profile())
        return MedicalAppointment.objects.all()
