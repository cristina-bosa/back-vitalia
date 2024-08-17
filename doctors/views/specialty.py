from rest_framework import viewsets

from doctors.models.specialty import Specialty
from doctors.serializers.specialty import SpecialtySerializer


class SpecialtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer