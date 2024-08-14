from rest_framework import viewsets

from patients.models.allergies import Allergies
from patients.serializers.allergies import AllergiesSelectSerializer, AllergiesSerializer


class AllergiesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AllergiesSelectSerializer
    queryset = Allergies.objects.all()

