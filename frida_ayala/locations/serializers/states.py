"""States serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.locations.models.states import State


class StateBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']
