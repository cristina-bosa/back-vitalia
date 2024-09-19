from datetime import datetime, timedelta

from http import HTTPStatus

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.choices.statusdoctor import StatusDoctor
from authentication.models.doctor import Doctor
from authentication.permissions.groups import IsUserPatient
from doctors.choices.status import Status
from doctors.models.medical_appointment import MedicalAppointment
from doctors.models.review import Review
from doctors.serializers.doctor import DoctorSerializer
from doctors.serializers.review import ReviewSerializer


class DoctorFilter(filters.FilterSet):
    city = filters.NumberFilter(field_name='user__city__id')
    specialty = filters.NumberFilter(field_name='specialty__id')

    class Meta:
        model = Doctor
        fields = ['city', 'specialty']


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DoctorFilter

    @action(detail=False, methods=['get'], url_path='confirmed')
    def get_active_doctors(self, request):
        doctors = Doctor.objects.filter(status=StatusDoctor.CONFIRMED)
        return Response(data=DoctorSerializer(doctors, many=True).data, status=HTTPStatus.OK)

    @action (detail = False, methods = ['get'], url_path = 'top')
    def get_top_four(self, request):
        user = request.user
        city = user.city
        doctors = Doctor.objects.filter(user__city = city)[:4]
        return Response(data = DoctorSerializer(doctors, many = True).data, status = HTTPStatus.OK)

    @action(detail=True, methods=['get'], url_path='reviews')
    def reviews(self, request):
        doctor = self.get_object()
        reviews = doctor.reviews_set.all()
        return Response(ReviewSerializer(reviews, many=True).data, status= HTTPStatus.OK)

    @action(detail=False, methods=['post'], url_path='review/add')
    def add_review(self, request):
        doctor = self.get_object()
        reviews = doctor.reviews_set.filter(patient = self.request.user.patient)
        if reviews.exists():
            return Response(data = "Ya has asignado una review a este médico",
                            status = HTTPStatus.FOUND)
        review_serializer = ReviewSerializer(data = request.data)
        review_serializer.is_valid()
        if review_serializer.errors:
            return Response(data = review_serializer.errors, status = HTTPStatus.BAD_REQUEST)
        review = Review.objects.create(
                rating = request.data.get('rating'),
                review = request.data.get('review'),
                doctor = doctor,
                patient = self.request.user.patient
                )
        self.__calculate_rating(doctor)
        return Response(data = ReviewSerializer(review).data, status = HTTPStatus.CREATED)

    @action(detail=False, methods=['delete'], url_path='review/<int:review_id>/delete')
    def delete_review(self, request, review_id):
        doctor = self.get_object()
        reviews = doctor.reviews_set.filter(id = review_id, patient = self.request.user.patient)
        for review in reviews:
            review.delete()
        self.__calculate_rating(doctor)
        return Response(status = HTTPStatus.NO_CONTENT)

    @action(detail=True, methods=['post'], url_path = "available-hours", permission_classes=[IsAuthenticated,
                                                                                            IsUserPatient])
    def available_hours(self, request, pk):
        data = request.data
        try:
            doctor = Doctor.objects.get(pk = pk)
        except Doctor.DoesNotExist:
            return Response(data = "Doctor no encontrado", status = HTTPStatus.NOT_FOUND)

        appointment_datetime = datetime.strptime(data['patient_appointment'], '%Y-%m-%d %H:%M:%S')
        date = appointment_datetime.date()

        appointments = MedicalAppointment.objects.filter(
                doctor = doctor,
                status = Status.CONFIRMED,
                patient_appointment__date = date,
                )

        confirmed_slots = appointments.values_list('patient_appointment', flat = True)
        occupied_slots = []
        for slot in confirmed_slots:
            hour = slot.hour
            occupied_slots.append(hour)

        today = datetime.now()
        start_working = datetime.combine(today, doctor.start_schedule).hour
        end_working = datetime.combine(today, doctor.end_schedule).hour
        doctor_slots = []
        for number in range(start_working, end_working+1):
            doctor_slots.append(number)

        slots_available = []
        for slot in doctor_slots:
            if slot not in occupied_slots:
                time_slot = datetime.combine(today, datetime.min.time()).replace(hour=slot).strftime('%H:%M')
                slots_available.append(time_slot)

        if not slots_available:
            return Response(data = "No hay horarios disponibles", status = HTTPStatus.NOT_FOUND)

        return Response(data = slots_available, status = HTTPStatus.OK)

    def __calculate_rating(self, doctor):
        reviews = doctor.reviews_set.all()
        total = 0
        for review in reviews:
            total += review.rating
        doctor.stars = total / reviews.count()
        doctor.save()
        return doctor.rating