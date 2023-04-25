"""States serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.locations.models.states import State
# Serializers
from frida_ayala.locations.serializers.municipalities import MunicipalityChoiceSerializer


class StateBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']


class StateChoiceModelSerializer(serializers.ModelSerializer):
    municipalities = MunicipalityChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['name', 'pk', 'municipalities']
