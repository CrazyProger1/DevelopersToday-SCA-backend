from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from src.apps.sca.serializers import (
    TargetListSerializer,
    TargetRetrieveSerializer,
)
from src.apps.sca.services.db import mark_target_completed, get_all_targets
from src.utils.django.serializers import EmptySerializer


class TargetViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_targets()
    serializer_class = TargetListSerializer
    serializer_classes = {
        "list": TargetListSerializer,
        "retrieve": TargetRetrieveSerializer,
        "mark_completed": EmptySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=["patch"], url_path="mark-completed")
    def mark_completed(self, request, pk=None):
        target = self.get_object()
        mark_target_completed(target=target)
        serializer = TargetRetrieveSerializer(target)
        return Response(serializer.data)
