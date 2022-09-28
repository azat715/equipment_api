from rest_framework import serializers

from main.models import Eqpt, EqptType


class EqptTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqptType
        fields = "__all__"


class EqptSerializer(serializers.ModelSerializer):
    eqpt_type_name = serializers.CharField(source="eqpt_type.name")

    def create(self, validated_data):
        eqpt_type_name = validated_data.pop("eqpt_type").pop("name")
        eqpt_type = EqptType.objects.get(name=eqpt_type_name)
        eqpt = Eqpt(eqpt_type=eqpt_type, **validated_data)
        eqpt.full_clean()  # тут необходимо переделать чтобы возвращалась не html страница а json response https://github.com/encode/django-rest-framework/issues/3144
        return eqpt.save()

    class Meta:
        model = Eqpt

        exclude = ["deleted", "eqpt_type"]
