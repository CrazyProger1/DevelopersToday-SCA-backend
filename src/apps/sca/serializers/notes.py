from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from src.apps.sca.models import Note


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class NoteRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class NoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("content",)


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("target", "content",)

    def validate(self, attrs):
        target = attrs.get('target')
        if target:
            if target.is_completed or target.mission.is_completed:
                raise PermissionDenied("Cannot create or update note of completed target or mission.")
        return attrs
