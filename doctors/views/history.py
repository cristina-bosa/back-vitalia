from rest_framework import viewsets

from doctors.choices.status import Status
from doctors.models.medical_appointment import MedicalAppointment
from doctors.serializers.medical_appointment import MedicalAppointmentSerializer


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MedicalAppointment.objects.filter(status = Status.FINISHED)
    serializer_class = MedicalAppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_patient():
            return MedicalAppointment.objects.filter(patient = user.get_profile())
        elif user.is_doctor():
            return MedicalAppointment.objects.filter(doctor = user.get_profile())
        return MedicalAppointment.objects.all()
