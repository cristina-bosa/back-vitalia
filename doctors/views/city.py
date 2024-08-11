from rest_framework import viewsets
from doctors.models.city import City
from doctors.serializers.city import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer