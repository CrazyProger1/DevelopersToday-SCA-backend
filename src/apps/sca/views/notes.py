from rest_framework import viewsets, mixins

from src.apps.sca.permissions import CanUpdateNoteUntilMissionOrTargetCompleted
from src.apps.sca.serializers import (
    NoteListSerializer,
    NoteRetrieveSerializer,
    NoteUpdateSerializer,
)
from src.apps.sca.services.db import get_all_notes


class NoteViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = get_all_notes()
    serializer_class = NoteListSerializer
    permission_classes = (CanUpdateNoteUntilMissionOrTargetCompleted,)
    serializer_classes = {
        "list": NoteListSerializer,
        "retrieve": NoteRetrieveSerializer,
        "update": NoteUpdateSerializer,
        "partial_update": NoteUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
