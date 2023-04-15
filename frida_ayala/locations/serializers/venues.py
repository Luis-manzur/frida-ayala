"""Venues Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.locations.models import Venue
from frida_ayala.locations.serializers.municipalities import MunicipalityBasicSerializer
# Serializers
from frida_ayala.locations.serializers.states import StateBasicSerializer


class VenueModelSerializer(serializers.ModelSerializer):
    """Venue model serializer."""
    state = StateBasicSerializer(read_only=True)
    municipality = MunicipalityBasicSerializer(read_only=True)

    class Meta:
        model = Venue
        exclude = ['created', 'modified']
