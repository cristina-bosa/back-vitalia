from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models.doctor import Doctor
from authentication.permissions.groups import IsUserAdmin
from authentication.serializers.user import UserSerializer


class DoctorAdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.filter(user__is_active=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserAdmin]
    @action(detail=True, methods=['post'], url_path='(activate|deactivate)')
    def manage_doctor(self, request):
        doctor = self.get_object()
        user = doctor.user
        user.is_active = request.path.endswith('activate')
        user.save()
        return Response(status=HTTPStatus.OK)

