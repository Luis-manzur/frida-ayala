"""EventDays serializers."""

from datetime import datetime

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models.shows import EventDay
from frida_ayala.events.serializers.itineraries import ItineraryModelSerializer
# Serializers
from frida_ayala.events.serializers.movies import MovieModelSerializer


class EventDayModelSerializer(serializers.ModelSerializer):
    """EventDay model serializer."""
    movies = MovieModelSerializer(read_only=True, many=True)
    itinerary = ItineraryModelSerializer(read_only=True, many=True, )

    class Meta:
        model = EventDay
        exclude = ['created', 'modified']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        formatted_date = datetime.strftime(date, '%d %b')
        data["itinerary"] = sorted(data["itinerary"], key=lambda x: x["start_time"])
        data['date'] = formatted_date
        return data
