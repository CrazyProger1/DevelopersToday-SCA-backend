from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

from src.apps.sca.services.db import can_update_note


class CanUpdateNoteUntilMissionOrTargetCompleted(permissions.BasePermission):
    message = _("Cannot create or update note of completed target or mission")

    def has_object_permission(self, request, view, obj):
        if request.method in {"PUT", "PATCH"}:
            return can_update_note(note=obj)

        return True
