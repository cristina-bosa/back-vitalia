from rest_framework import viewsets


from patients.models.relevant_diseases import RelevantDiseases
from patients.serializers.relevant_diseases import RelevantDiseasesSerializer


class RelevantDiseasesViewSet(viewsets.ModelViewSet):
    serializer_class = RelevantDiseasesSerializer
    queryset = RelevantDiseases.objects.all()
