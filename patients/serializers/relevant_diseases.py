from rest_framework import serializers

from patients.models.relevant_diseases import RelevantDiseases


class RelevantDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelevantDiseases
        fields = '__all__'

