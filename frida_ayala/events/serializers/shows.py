"""EventDays serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models.shows import EventDay
# Serializers
from frida_ayala.events.serializers.movies import MovieModelSerializer


class EventDayModelSerializer(serializers.ModelSerializer):
    """EventDay model serializer."""
    movies = MovieModelSerializer(read_only=True, many=True)

    class Meta:
        model = EventDay
        exclude = ['created', 'modified']
