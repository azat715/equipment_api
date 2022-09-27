from rest_framework import serializers

from main.models import Eqpt, EqptType


class EqptTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqptType
        fields = "__all__"


class EqptSerializer(serializers.ModelSerializer):
    eqpt_type_name = serializers.CharField(source="eqpt_type.name")

    class Meta:
        model = Eqpt

        exclude = ["deleted", "eqpt_type"]
