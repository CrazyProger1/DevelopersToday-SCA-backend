from rest_framework import serializers

from src.apps.sca.models import Target


class TargetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class TargetRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class TargetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = (
            "name",
            "country",
        )
