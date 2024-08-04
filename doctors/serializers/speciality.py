from rest_framework import serializers

from doctors.models.speciality import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'

