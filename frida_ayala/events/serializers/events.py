"""Events serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models import Event


class EventModelSerializer(serializers.ModelSerializer):
    """Event model serializer."""

    class Meta:
        model = Event
        exclude = ['created', 'modified']
