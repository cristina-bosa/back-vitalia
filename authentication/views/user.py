from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from authentication.serializers.patient import PatientSerializer
from authentication.serializers.user import UserSerializer
from doctors.serializers.doctor import DoctorSerializer


class UserViewSet(viewsets.ViewSet):

    @action(detail = False, methods = ['get'], url_path = 'profile', permission_classes = [IsAuthenticated])
    def profile(self, request):
        user = request.user
        if user.groups.filter(name = 'Patient').exists():
            user = Patient.objects.get(user = user)
            return Response(data = PatientSerializer(user).data)
        elif user.groups.filter(name = 'Doctor').exists():
            user = Doctor.objects.get(user = user)
            return Response(data = DoctorSerializer(user).data)
        return Response(data = UserSerializer(user).data)

    @action(detail = False, methods = ['post'], url_path = 'update-profile', permission_classes = [IsAuthenticated])
    def update_profile(self, request):
        #TODO: Implementar el endpoint de actualizar perfil
        pass

    @action(detail = False, methods = ['post'], url_path = 'cancel-account', permission_classes = [IsAuthenticated]) #cancel-account
    def cancel_account(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response(status = HTTPStatus.OK)