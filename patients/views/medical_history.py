from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_history import MedicalHistory
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases
from patients.serializers.medical_history import MedicalHistoryGetSerializer


class MedicalHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedicalHistoryGetSerializer
    queryset = MedicalHistory.objects.all()

    @action(detail = False, methods = ['post'], url_path = 'allergies/add')
    def add_allergy(self, request):
        medical_history = self.__get_user_medical_history(request)
        allergies = Allergies.objects.filter(pk__in = request.data['history_id'])
        for allergy in allergies:
            medical_history.allergies.add(allergy)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'allergies/remove')
    def remove_allergy(self, request):
        medical_history = self.__get_user_medical_history(request)
        try:
            allergy = Allergies.objects.get(name = request.data['history_id'])
        except Allergies.DoesNotExist:
            return Response(data = { 'error': 'Allergy not found' }, status = HTTPStatus.NOT_FOUND)
        medical_history.allergies.remove(allergy)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'relevant-diseases/add')
    def add_relevant_disease(self, request):
        medical_history = self.__get_user_medical_history(request)
        relevant_diseases = RelevantDiseases.objects.filter(pk__in = request.data['history_id'])
        for relevant in relevant_diseases:
            medical_history.relevant_diseases.add(relevant)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'relevant-diseases/remove')
    def remove_relevant_disease(self, request):
        medical_history = self.__get_user_medical_history(request)
        try:
            relevant_diseases = RelevantDiseases.objects.get(name = request.data['history_id'])
        except RelevantDiseases.DoesNotExist:
            return Response(data = {'error': 'RelevantDiseases not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.relevant_diseases.remove(relevant_diseases)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'current-medication/add')
    def add_current_medication(self, request):
        medical_history = self.__get_user_medical_history(request)
        current_medication = CurrentMedication.objects.filter(pk__in = request.data['history_id'])
        for current in current_medication:
            medical_history.current_medication.add(current)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'current-medication/remove')
    def remove_current_medication(self, request):
        medical_history = self.__get_user_medical_history(request)
        try:
            current_medication = CurrentMedication.objects.get(name = request.data['history_id'])
        except CurrentMedication.DoesNotExist:
            return Response(data = {'error': 'CurrentMedication not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.current_medication.remove(current_medication)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'medical-intervention/add')
    def add_medical_intervention(self, request):
        medical_history = self.__get_user_medical_history(request)
        medical_intervention = MedicalIntervention.objects.filter(pk__in = request.data['history_id'])
        for medical in medical_intervention:
            medical_history.medical_intervention.add(medical)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'medical-intervention/remove')
    def remove_medical_intervention(self, request):
        medical_history = self.__get_user_medical_history(request)
        try:
            medical_intervention = MedicalIntervention.objects.get(name = request.data['history_id'])
        except MedicalIntervention.DoesNotExist:
            return Response(data = {'error': 'MedicalIntervention not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.medical_intervention.remove(medical_intervention)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    def __get_user_medical_history(self, request):
        user = request.user
        return user.get_profile().medical_history