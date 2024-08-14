from rest_framework import viewsets


from patients.models.relevant_diseases import RelevantDiseases
from patients.serializers.relevant_diseases import RelevantDiseasesSelectSerializer


class RelevantDiseasesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RelevantDiseasesSelectSerializer
    queryset = RelevantDiseases.objects.all()
