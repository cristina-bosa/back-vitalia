from rest_framework import serializers

from doctors.models.city import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

