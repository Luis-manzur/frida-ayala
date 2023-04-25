"""Event day models."""

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class EventDay(FAModel):
    """EventDay model."""

    event = models.ForeignKey('events.Event', related_name='show', on_delete=models.CASCADE)
    date = models.DateField('Show Date', null=False)
    start_time = models.TimeField('Show start time')
    end_time = models.TimeField('Show end time', )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        """Return event's str representation."""
        return f'{self.event} ({self.date})'
