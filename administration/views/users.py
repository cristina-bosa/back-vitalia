from datetime import datetime, timedelta

from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from administration.serializers.users import UserDoctorSerializer, Userserializer
from authentication.choices.statusdoctor import StatusDoctor
from authentication.models import User
from django.db.models import Q
from authentication.permissions.groups import IsUserAdmin


class UserAdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(Q(groups__name='Patient') | Q(groups__name='Doctor', doctor__status=StatusDoctor.CONFIRMED))
    serializer_class = Userserializer
    permission_classes = [IsAuthenticated, IsUserAdmin]

    @action(detail=True, methods=['post'], url_path='(?P<admin_action>(activate|deactivate))')
    def manage_users(self, request, pk, *args, **kwargs, ):
        admin_action = kwargs.get('admin_action')
        user = User.objects.get(pk=pk)
        if admin_action == 'activate':
            user.is_active = True
            user.save()
            return Response(data= 'Se ha activado el usuario', status=HTTPStatus.OK)
        if admin_action == 'deactivate':
            user.is_active = False
            user.save()
            return Response(data= 'Se ha desactivado al usuario', status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='last-(?P<admin_action>(patients|doctors))')
    def last_registrations(self, request, *args, **kwargs):
        admin_action = kwargs.get('admin_action')
        queryset = User.objects.filter(
            Q(groups__name = 'Patient') | Q(groups__name = 'Doctor', doctor__status__in= [StatusDoctor.PENDING,
                                                                                         StatusDoctor.CONFIRMED]))

        one_month_ago = datetime.now() - timedelta(days=30)

        if admin_action == 'patients':
            patients = queryset.filter(date_joined__gte = one_month_ago, groups__name = 'Patient')
            if not patients.exists():
                return Response(data='No hay pacientes registrados en el último mes', status=HTTPStatus.NOT_FOUND)
            serializer = Userserializer(patients, many=True)
            return Response(serializer.data, HTTPStatus.OK)

        if admin_action == 'doctors':
            doctors = queryset.filter(date_joined__gte=one_month_ago, groups__name='Doctor')
            if not doctors.exists():
                return Response(data = 'No hay doctores registrados en el último mes', status = HTTPStatus.NOT_FOUND)
            serializer = UserDoctorSerializer(doctors, many = True)
            return Response(serializer.data, HTTPStatus.OK)

