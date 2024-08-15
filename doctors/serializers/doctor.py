from rest_framework import serializers

from authentication.models.doctor import Doctor
from authentication.serializers.user import UserProfileSerializer


class DoctorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    city = serializers.CharField(source='user.city.name', read_only=True)
    specialty = serializers.CharField(source='specialty.name', read_only=True)
    class Meta:
        model = Doctor
        fields = '__all__'

