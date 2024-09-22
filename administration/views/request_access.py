from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from administration.serializers.request_access import RequestAccessSerializer
from authentication.choices.statusdoctor import StatusDoctor
from authentication.models.doctor import Doctor
from authentication.permissions.groups import IsUserAdmin


class RequestAccessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.filter(status__in=[StatusDoctor.PENDING])
    serializer_class = RequestAccessSerializer
    permission_classes = [IsAuthenticated, IsUserAdmin]

    @action(detail=True, methods=['post'], url_path='(?P<admin_action>(accept|reject))')
    def manage_doctor(self, request, admin_action,pk):
        doctor = Doctor.objects.get(pk=pk)
        if admin_action == 'accept':
            doctor.status = StatusDoctor.CONFIRMED
            doctor.save()
            return Response(data= 'Se ha aceptado al médico', status=HTTPStatus.OK)
        if admin_action == 'reject':
            doctor.status = StatusDoctor.CANCELED
            doctor.save()
            return Response(data ='Se ha rechazado al médico', status = HTTPStatus.OK)

