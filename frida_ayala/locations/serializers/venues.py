"""Venues Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.locations.models import Venue


class VenueModelSerializer(serializers.ModelSerializer):
    """Venue model serializer."""

    class Meta:
        model = Venue
        exclude = ['created', 'modified']
