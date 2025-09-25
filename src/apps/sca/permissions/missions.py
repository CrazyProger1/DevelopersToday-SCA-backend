from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

from src.apps.sca.services.db import is_mission_assigned


class CanDeleteMissionIfNotAssigned(permissions.BasePermission):
    message = _("Cannot delete mission assigned to a cat")

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return not is_mission_assigned(mission=obj)

        return True
