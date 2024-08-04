from rest_framework import serializers

from doctors.models.medical_attachment import MedicalAttachment


class MedicalAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAttachment
        fields = '__all__'

