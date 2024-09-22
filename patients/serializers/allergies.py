from rest_framework import serializers

from patients.models.allergies import Allergies


class AllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = '__all__'


class AllergiesSelectSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = Allergies
        fields = ['value','label']