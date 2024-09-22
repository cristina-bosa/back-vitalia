from rest_framework import serializers

from patients.models.relevant_diseases import RelevantDiseases


class RelevantDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelevantDiseases
        fields = '__all__'

class RelevantDiseasesSelectSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = RelevantDiseases
        fields = ['value','label']