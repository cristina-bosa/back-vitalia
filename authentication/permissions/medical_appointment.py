from rest_framework.permissions import BasePermission

from doctors.choices.status import Status


class IsMedicalAppointmentPending(BasePermission):
    message = 'La cita debe estar en estado pendiente'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.PENDING


class IsMedicalAppointmentConfirmed(BasePermission):
    message = 'La cita debe estar en estado confirmado'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.CONFIRMED


class IsMedicalAppointmentInProgress(BasePermission):
    message = 'La cita debe estar en estado en progreso'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.IN_PROGRESS


class IsMedicalAppointmentCanceled(BasePermission):
    message = 'La cita debe estar en estado cancelado'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.CANCELED


class IsMedicalAppointmentFinished(BasePermission):
    message = 'La cita debe estar en estado finalizado'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.FINISHED


class IsMedicalAppointmentPendingOrConfirmed(BasePermission):
    message = 'La cita debe estar en estado pendiente o confirmado'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.PENDING or obj.status == Status.CONFIRMED


class IsMedicalAppointmentCanceledOrFinished(BasePermission):
    message = 'La cita debe estar en estado cancelado o finalizado'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.CANCELED or obj.status == Status.FINISHED

class IsMedicalAppointmentInprogressOrFinished(BasePermission):
    message = 'La cita debe estar en estado en progreso o finalizado'

    def has_object_permission(self, request, view, obj):
        return obj.status == Status.IN_PROGRESS or obj.status == Status.FINISHED