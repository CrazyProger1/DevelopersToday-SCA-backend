from rest_framework import serializers

from src.apps.sca.models import Breed


class BreedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
