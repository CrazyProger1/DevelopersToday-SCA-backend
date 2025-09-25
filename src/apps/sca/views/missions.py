from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from src.apps.sca.permissions import CanDeleteMissionIfNotAssigned
from src.apps.sca.serializers import (
    MissionCreateSerializer,
    MissionListSerializer,
    MissionRetrieveSerializer,
    MissionAssignSerializer,
)
from src.apps.sca.services.db import (
    get_all_missions,
    assign_cat_to_mission,
    mark_mission_completed,
)
from src.utils.django.serializers import EmptySerializer


class MissionViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = get_all_missions()
    serializer_class = MissionListSerializer
    permission_classes = (CanDeleteMissionIfNotAssigned,)
    serializer_classes = {
        "create": MissionCreateSerializer,
        "list": MissionListSerializer,
        "retrieve": MissionRetrieveSerializer,
        "assign": MissionAssignSerializer,
        "mark_completed": EmptySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=["patch"], url_path="assign-cat")
    def assign(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get("cat_id")
        assign_cat_to_mission(
            mission=mission,
            cat_id=cat_id,
        )
        serializer = MissionRetrieveSerializer(mission)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"], url_path="mark-completed")
    def mark_completed(self, request, pk=None):
        mission = self.get_object()
        mark_mission_completed(mission=mission)
        serializer = MissionRetrieveSerializer(mission)
        return Response(serializer.data)
