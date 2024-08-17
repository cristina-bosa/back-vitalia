from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from patients.models.allergies import Allergies
from patients.models.current_medication import CurrentMedication
from patients.models.medical_history import MedicalHistory
from patients.models.medical_intervention import MedicalIntervention
from patients.models.relevant_diseases import RelevantDiseases
from patients.serializers.medical_history import MedicalHistorySerializer


class MedicalHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedicalHistorySerializer
    queryset = MedicalHistory.objects.all()

    @action(detail = True, methods = ['post'], url_path = 'allergies/add/<int:allergy_id>')
    def add_allergy(self, request, allergy_id = None):
        medical_history = self.get_object()
        try:
            allergy = Allergies.objects.get(pk = allergy_id)
        except Allergies.DoesNotExist:
            return Response(data = {'error': 'Allergy not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.allergies.add(allergy)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)


    @action(detail = True, methods = ['post'], url_path = 'allergies/remove/<int:allergy_id>')
    def remove_allergy(self, request, allergy_id = None):
        medical_history = self.get_object()
        try:
            allergy = Allergies.objects.get(pk = allergy_id)
        except Allergies.DoesNotExist:
            return Response(data = { 'error': 'Allergy not found' }, status = HTTPStatus.NOT_FOUND)
        medical_history.allergies.delete(allergy)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.NO_CONTENT)

    @action(detail = True, methods = ['post'], url_path = 'relevant_diseases/add/<int:disease_id>')
    def add_relevant_disease(self, request, disease_id = None):
        medical_history = self.get_object()
        try:
            relevant_diseases = RelevantDiseases.objects.get(pk = disease_id)
        except RelevantDiseases.DoesNotExist:
            return Response(data = {'error': 'RelevantDiseases not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.relevant_diseases.add(relevant_diseases)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = True, methods = ['post'], url_path = 'relevant_diseases/remove/<int:disease_id>')
    def remove_relevant_disease(self, request, disease_id = None):
        medical_history = self.get_object()
        try:
            relevant_diseases = RelevantDiseases.objects.get(pk = disease_id)
        except RelevantDiseases.DoesNotExist:
            return Response(data = {'error': 'RelevantDiseases not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.relevant_diseases.delete(relevant_diseases)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.NO_CONTENT)

    @action(detail = True, methods = ['post'], url_path = 'current_medication/add/<int:medication_id>')
    def add_current_medication(self, request, medication_id = None):
        medical_history = self.get_object()
        try:
            current_medication = CurrentMedication.objects.get(pk = medication_id)
        except CurrentMedication.DoesNotExist:
            return Response(data = {'error': 'CurrentMedication not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.current_medication.add(current_medication)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = True, methods = ['post'], url_path = 'current_medication/remove/<int:medication_id>')
    def remove_current_medication(self, request, medication_id = None):
        medical_history = self.get_object()
        try:
            current_medication = CurrentMedication.objects.get(pk = medication_id)
        except CurrentMedication.DoesNotExist:
            return Response(data = {'error': 'CurrentMedication not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.current_medication.delete(current_medication)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.NO_CONTENT)

    @action(detail = True, methods = ['post'], url_path = 'medical_intervention/add/<int:intervention_id>')
    def add_medical_intervention(self, request, intervention_id = None):
        medical_history = self.get_object()
        try:
            medical_intervention = MedicalIntervention.objects.get(pk = intervention_id)
        except MedicalIntervention.DoesNotExist:
            return Response(data = {'error': 'MedicalIntervention not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.medical_intervention.add(medical_intervention)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.ACCEPTED)

    @action(detail = True, methods = ['post'], url_path = 'medical_intervention/remove/<int:intervention_id>')
    def remove_medical_intervention(self, request, intervention_id = None):
        medical_history = self.get_object()
        try:
            medical_intervention = MedicalIntervention.objects.get(pk = intervention_id)
        except MedicalIntervention.DoesNotExist:
            return Response(data = {'error': 'MedicalIntervention not found'}, status = HTTPStatus.NOT_FOUND)
        medical_history.medical_intervention.delete(medical_intervention)
        return Response(data = self.serializer_class(medical_history).data, status = HTTPStatus.NO_CONTENT)