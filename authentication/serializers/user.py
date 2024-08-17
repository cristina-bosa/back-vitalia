from rest_framework import serializers

from authentication.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'birth_date', 'genre', 'phone','identification_number', 'groups',