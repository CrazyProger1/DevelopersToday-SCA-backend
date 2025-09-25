from rest_framework import viewsets, mixins

from src.apps.sca.services.db import get_all_breeds
from src.apps.sca.serializers import BreedListSerializer


class BreedViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_breeds()
    serializer_class = BreedListSerializer
