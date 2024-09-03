from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from authentication.permissions.groups import IsUserAdmin
from authentication.serializers.user import UserSerializer


class UserAdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserAdmin]
