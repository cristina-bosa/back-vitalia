from rest_framework.permissions import BasePermission


class IsUserPatient(BasePermission):
    message = 'Debes ser un paciente para acceder a este recurso'

    def has_permission(self, request, view):
        return request.user.is_patient() or request.user.is_admin()


class IsUserDoctor(BasePermission):
    message = 'Debes ser un doctor para acceder a este recurso'

    def has_permission(self, request, view):
        return request.user.is_doctor() or request.user.is_admin()


class IsUserAdmin(BasePermission):
    message = 'Debes ser un administrador para acceder a este recurso'

    def has_permission(self, request, view):
        return request.user.is_admin()