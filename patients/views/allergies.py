from rest_framework import viewsets

from patients.models.allergies import Allergies
from patients.serializers.allergies import AllergiesSerializer


class AllergiesViewSet(viewsets.ModelViewSet):
    serializer_class = AllergiesSerializer
    queryset = Allergies.objects.all()

