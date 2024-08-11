from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.choices.genre import Genre
from doctors.choices.status import Status


class ChoicesViewSet(viewsets.ViewSet):
    permission_classes = []

    @action(detail=False, methods=['get'], url_path='genre')
    def genre(self, request):
        return Response(data=[{'id':v, 'name': k} for k, v in Genre.choices], status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='status')
    def status(self, request):
        return Response(data=Status.choices, status=HTTPStatus.OK)
