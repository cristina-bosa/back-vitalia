from http import HTTPStatus

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from authentication.models import User
from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from authentication.serializers.doctor import DoctorSerializer
from authentication.serializers.patient import PatientSerializer
from authentication.serializers.user import UserSerializer
from authentication.utils.type_user import REGISTER_TYPE
from patients.models.medical_history import MedicalHistory
from patients.serializers.medical_history import MedicalHistoryGetSerializer, MedicalHistorySerializer


class AuthViewSet(viewsets.ViewSet):
    @action(detail = False, methods = ['post'], url_path = 'register') #register
    def register(self, request):
        try:
            register_type = request.data.get('register_type')
            if not register_type in REGISTER_TYPE:
                return HTTPStatus.BAD_REQUEST

            user_serializer = UserSerializer(data = request.data)
            user_serializer.is_valid()
            if user_serializer.errors:
                return Response(data = user_serializer.errors, status = HTTPStatus.BAD_REQUEST)

            if register_type == REGISTER_TYPE.DOCTOR:
                profile_serializer = DoctorSerializer
                profile_data = request.data
            else:
                profile_serializer = MedicalHistorySerializer
                profile_data = request.data.get('medical_history', {})
            profile_serializer = profile_serializer(data = profile_data)
            profile_serializer.is_valid()
            if profile_serializer.errors:
                return Response(data = profile_serializer.errors, status = HTTPStatus.BAD_REQUEST)

            user = user_serializer.save()
            user.set_password(user.password)
            user.save()
            if register_type == REGISTER_TYPE.DOCTOR:
                doctor = Doctor.objects.create(**profile_serializer.validated_data, user = user)
                user.groups.add(Group.objects.get(name = 'Doctor'))
            else:
                medical_history = profile_serializer.save()
                patient = Patient.objects.create(
                    user = user,
                    medical_history = medical_history
                )
                user.groups.add(Group.objects.get(name = 'Patient'))

            return Response(data = 'Usuario creado con éxito', status = HTTPStatus.CREATED)

        except Exception as e:
            raise e

    @action(detail = False, methods = ['post'], url_path = 'login', permission_classes = []) #login
    def login(self, request):
        user = self.request.user
        if not user or not user.is_authenticated:
            user = authenticate(**request.data)
        if user and not user.is_anonymous:
            login(request, user)
        if not user or user.is_anonymous:
            return Response({'detail': 'Invalid credentials or activate account'}, status=HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user = user)
        return Response({'access_token': token.key}, status=HTTPStatus.OK)

    @action(detail = False, methods = ['post'], url_path = 'logout', permission_classes = [IsAuthenticated]) #logout
    def logout(self, request):
        logout(request)
        return Response(status=200)

    @action(detail = False, methods = ['get'], url_path = 'forgot-password', permission_classes = []) #forgot-password
    def forgot_password(self, request):
        email, identification_number = request.data.get('email'), request.data.get('identification_number')
        try:
            user = User.objects.get(email = email, identification_number = identification_number, is_active = True)
        except:
            return Response(data = "Usuario no identificado", status = HTTPStatus.NOT_FOUND)
        new_password = request.data.get('password')
        user.set_password(new_password)
        user.save()
        return Response(data = "La contraseña ha sido actualizada con éxito", status = HTTPStatus.OK)
