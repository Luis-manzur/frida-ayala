"""Events serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models import Event
# Serializers
from frida_ayala.locations.serializers.venues import VenueModelSerializer


class EventModelSerializer(serializers.ModelSerializer):
    """Event model serializer."""
    venue = VenueModelSerializer(read_only=True)

    class Meta:
        model = Event
        exclude = ['created', 'modified']
