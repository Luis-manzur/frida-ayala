"""schedule day models."""

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Itinerary(FAModel):
    """Itinerary model"""
    name = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    event_day = models.ForeignKey('events.EventDay', related_name='itinerary', on_delete=models.CASCADE)
