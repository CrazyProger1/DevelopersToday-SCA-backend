from rest_framework import serializers

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
