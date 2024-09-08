from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from authentication.serializers.patient import PatientSerializer
from authentication.serializers.user import UpdateProfileSerializer, UserSerializer
from doctors.serializers.doctor import DoctorSerializer


class UserViewSet(viewsets.ViewSet):

    @action(detail = False, methods = ['get'], url_path = 'profile', permission_classes = [IsAuthenticated])
    def profile(self, request):
        user = self.request.user
        if user.is_patient():
            user = Patient.objects.get(user = user)
            return Response(data = PatientSerializer(user).data)
        if user.is_doctor():
            user = Doctor.objects.get(user = user)
            return Response(data = DoctorSerializer(user).data)
        return Response(data = UserSerializer(user).data)

    @action(detail = False, methods = ['post'], url_path = 'update-profile', permission_classes = [IsAuthenticated])
    def update_profile(self, request):
        user = self.request.user
        serializer = UpdateProfileSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            if user.is_patient():
                patient = Patient.objects.get(user = user)
                patient.save()
            elif user.is_doctor():
                doctor = Doctor.objects.get(user = user)
                doctor.save()
            return Response(data = serializer.data, status = HTTPStatus.OK)
        return Response(data = serializer.errors, status = HTTPStatus.BAD_REQUEST)

    @action(detail = False, methods = ['post'], url_path = 'cancel-account', permission_classes = [IsAuthenticated]) #cancel-account
    def cancel_account(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response(status = HTTPStatus.OK)