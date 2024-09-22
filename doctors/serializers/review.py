from rest_framework import serializers

from doctors.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewDoctorSerializer(serializers.ModelSerializer):
    patient_name = serializers.StringRelatedField(source='patient.user.first_name', read_only=True)
    patient_last_name = serializers.StringRelatedField(source='patient.user.last_name', read_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Review
        fields = ['id', 'patient_name', 'patient_last_name', 'rating', 'review', 'created_at']