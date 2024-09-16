from rest_framework import serializers

from authentication.models.doctor import Doctor


class RequestAccessSerializer(serializers.ModelSerializer):
    specialty = serializers.CharField(source='specialty.name', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only = True, format = '%d-%m-%Y')
    class Meta:
        model = Doctor
        fields = ['id', 'professional_number', 'specialty', 'status', 'first_name', 'last_name', 'email', 'phone', 'date_joined']