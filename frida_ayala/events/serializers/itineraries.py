"""Itineraries serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models import Itinerary


# Serializers


class ItineraryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        exclude = ['created', 'modified', 'event_day']
        ordering = ['created']
