"""EventDays serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models.shows import EventDay


class EventDayModelSerializer(serializers.ModelSerializer):
    """EventDay model serializer."""

    class Meta:
        model = EventDay
        exclude = ['created', 'modified']
