from rest_framework import serializers

from src.apps.sca.models import Cat


class CatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        exclude = (
            "image",
            "id",
        )


class CatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"


class CatRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"


class CatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ("salary",)
