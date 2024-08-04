from rest_framework import serializers

from patients.models.allergies import Allergies


class AllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = '__all__'

