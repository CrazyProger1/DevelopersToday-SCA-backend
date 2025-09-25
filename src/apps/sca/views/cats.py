from rest_framework import viewsets

from src.apps.sca.serializers.cats import CatCreateSerializer
from src.apps.sca.services.db import get_all_cats
from src.apps.sca.serializers import (
    CatUpdateSerializer,
    CatRetrieveSerializer,
    CatListSerializer,
)


class CatViewSet(
    viewsets.ModelViewSet,
):
    queryset = get_all_cats()
    serializer_class = CatListSerializer
    serializer_classes = {
        "create": CatCreateSerializer,
        "list": CatListSerializer,
        "retrieve": CatRetrieveSerializer,
        "update": CatUpdateSerializer,
        "partial_update": CatUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
