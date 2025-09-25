from rest_framework import serializers
from src.apps.sca.models import Mission
from django.utils.translation import gettext_lazy as _

from src.apps.sca.serializers import (
    TargetCreateSerializer,
    TargetRetrieveSerializer,
    CatRetrieveSerializer,
)
from src.apps.sca.services.db import get_all_cats


class MissionCreateSerializer(serializers.ModelSerializer):
    targets = TargetCreateSerializer(many=True)

    class Meta:
        model = Mission
        fields = (
            "cat",
            "targets",
        )

    def create(self, validated_data):
        targets = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)
        for target in targets:
            TargetCreateSerializer().create({**target, "mission": mission})
        return mission


class MissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            "id",
            "cat",
            "is_completed",
            "created_at",
            "updated_at",
        )


class MissionRetrieveSerializer(serializers.ModelSerializer):
    cat = CatRetrieveSerializer(read_only=True)
    targets = TargetRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = (
            "id",
            "cat",
            "is_completed",
            "targets",
            "created_at",
            "updated_at",
        )


class MissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            "cat",
            "is_completed",
        )

    def validate(self, data):
        if data.get("is_completed") and self.instance and self.instance.cat is None:
            raise serializers.ValidationError(
                _("Completed mission must have an assigned cat")
            )
        return data


class MissionAssignSerializer(serializers.Serializer):
    cat_id = serializers.PrimaryKeyRelatedField(queryset=get_all_cats())

    class Meta:
        fields = "__all__"
