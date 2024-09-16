from rest_framework import serializers

from authentication.models import User

class Userserializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format = '%d-%m-%Y')
    groups = serializers.StringRelatedField(many=True)
    date_joined = serializers.DateTimeField(read_only = True, format = '%d-%m-%Y')

    class Meta:
        model = User
        fields = ['id','is_active','first_name','identification_number','date_joined','last_name', 'email', 'phone', 'birth_date', 'genre', 'groups']

class UserDoctorSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format = '%d-%m-%Y')
    groups = serializers.StringRelatedField(many = True)
    date_joined = serializers.DateTimeField(read_only = True, format = '%d-%m-%Y')
    status = serializers.CharField(source = 'doctor.status')

    class Meta:
        model = User
        fields = ['id','is_active','first_name','identification_number','date_joined','last_name', 'email', 'phone', 'birth_date', 'genre', 'status', 'groups']
