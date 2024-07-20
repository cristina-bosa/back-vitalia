from http import HTTPStatus

from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from authentication.models.doctor import Doctor
from authentication.models.patient import Patient
from authentication.serializers.user import UserSerializer
from authentication.utils.type_user import REGISTER_TYPE


class AuthViewSet(viewsets.ViewSet):
    @action(detail = False, methods = ['post'], url_path = 'register') #register
    def register(self, request):
        try:
            type_register = request.data['type_register']

            if not type_register in REGISTER_TYPE:
                return HTTPStatus.BAD_REQUEST

            user_serializer = UserSerializer(data = request.data)
            user_serializer.is_valid()
            if user_serializer.errors:
                return Response(data = user_serializer.errors, status = HTTPStatus.BAD_REQUEST)

            if (not self.__validate_patient_data(request.data) and type_register is REGISTER_TYPE.PATIENT or not
                    self.__validate_doctor_data(request.data) and type_register is REGISTER_TYPE.DOCTOR):
                return Response(data = { 'msg': 'Invalid profile data' }, status = HTTPStatus.BAD_REQUEST)

            user = self.__create_user(request.data)

            if type_register is REGISTER_TYPE.PATIENT:
                Patient.objects.create({
                    'user': user,
                    'birth_date': request.data.get('birth_date'),
                    'genre': request.data.get('genre'),
                    })
                return Response(data = { 'msg': 'User created successfully' }, status = HTTPStatus.CREATED)

            elif type_register is REGISTER_TYPE.DOCTOR:
                Doctor.objects.create({
                    'user': user,
                    'specialty': request.data.get('specialty'),
                    })
                return Response(data = { 'msg': 'User created successfully' }, status = HTTPStatus.CREATED)

        except Exception as e:
            return Response(status = HTTPStatus.BAD_REQUEST)

    @action(detail = False, methods = ['post'], url_path = 'login', permission_classes = []) #login
    def login(self, request):
        pass

    @action(detail = False, methods = ['post'], url_path = 'logout', permission_classes = [IsAuthenticated]) #logout
    def logout(self, request):
        pass

    def __validate_doctor_data(self, data):
        condition = []
        condition.append(data.get('specialty') is not None)
        return all(condition)

    def __validate_patient_data(self, data):
        condition = []
        condition.append(data.get('birth_date') is not None)
        condition.append(data.get('genre') is not None)
        return all(condition)

    def __validate_user_data(self, data):
        condition = []
        condition.append(data.get('first_name') is not None)
        condition.append(data.get('last_name') is not None)
        condition.append(data.get('username') is not None)
        condition.append(data.get('email') is not None)
        condition.append(data.get('password') is not None)
        condition.append(data.get('phone') is not None)
        return all(condition)

    def __create_user(self, data):
        try:
            user = User.objects.create(
                username= data.get('username'),
                first_name= data.get('first_name'),
                last_name= data.get('last_name'),
                email= data.get('email'),
                password= data.get('password'),
                phone= data.get('phone'),
                )
            return user
        except Exception as e:
            return None

