from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.models.doctor import Doctor
from doctors.models.review import Review
from doctors.serializers.doctor import DoctorSerializer
from doctors.serializers.review import ReviewSerializer


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=False, methods=['post'], url_path='book')
    def book(self, request):
        pass

    @action(detail=False, methods=['post'], url_path='unbook')
    def unbook(self, request):
        pass

    @action(detail=False, methods=['get'], url_path='reviews')
    def reviews(self, request):
        doctor = self.get_object()
        reviews = doctor.reviews_set.all()
        return Response(ReviewSerializer(reviews, many=True).data, status= HTTPStatus.OK)

    @action(detail=False, methods=['post'], url_path='review/add')
    def add_review(self, request):
        doctor = self.get_object()
        reviews = doctor.reviews_set.filter(patient = self.request.user.patient)
        if reviews.exists():
            return Response(data = "Este doctor ya tiene una review asignada", status = HTTPStatus.FOUND)
        review_serializer = ReviewSerializer(data = request.data)
        review_serializer.is_valid()
        if review_serializer.errors:
            return Response(data = review_serializer.errors, status = HTTPStatus.BAD_REQUEST)
        review = review_serializer.create(request.data)
        review.doctor = doctor
        review.patient = self.request.user.patient
        review.save()
        return Response(data = ReviewSerializer(review).data, status = HTTPStatus.CREATED)

    @action(detail=False, methods=['delete'], url_path='review/<int:review_id>/delete')
    def delete_review(self, request, review_id):
        doctor = self.get_object()
        reviews = doctor.reviews_set.filter(id = review_id, patient = self.request.user.patient)
        for review in reviews:
            review.delete()
        return Response(status = HTTPStatus.NO_CONTENT)
