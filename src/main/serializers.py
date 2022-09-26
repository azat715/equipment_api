from rest_framework import serializers

from models import Eqpt, EqptType


class EqptTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EqptType
        fields = ['__all__']
