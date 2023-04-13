"""Event day models."""

# Django
from django.db import models

# Models
from frida_ayala.events.models import Event
# Utilities
from frida_ayala.utils.models import FAModel


class EventDay(FAModel):
    """EventDay model."""

    event = models.ForeignKey(Event, related_name='show', on_delete=models.CASCADE)
    date = models.DateField('Show Date', null=False)
    start_time = models.TimeField('Show start time')
    end_time = models.TimeField('Show end time', )

    class Meta:
        ordering = ['-created']
