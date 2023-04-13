"""Events models."""

# Django
from django.db import models

# Models
from frida_ayala.locations.models import Venue
# Utilities
from frida_ayala.utils.models import FAModel
from frida_ayala.utils.validators import validate_event_time


class Event(FAModel):
    """Event model."""
    TYPES = [
        ('B', 'Banff'),
        ('S', 'Seminar'),
        ('O', 'Other')
    ]
    start_date = models.DateField('Show start time', validators=[validate_event_time])
    end_date = models.DateField('Show end time', validators=[validate_event_time])
    name = models.CharField('Event name', max_length=120)
    slug_name = models.SlugField(unique=True, max_length=40)
    banner = models.ImageField(upload_to='events/banners', unique=True)
    about = models.CharField('event description', max_length=255)
    venue = models.ForeignKey(Venue, related_name='venue', null=True, on_delete=models.SET_NULL)
    type = models.CharField(choices=TYPES, default='B', max_length=150)

    class Meta:
        indexes = [
            models.Index(fields=['slug_name'])
        ]
        ordering = ['-created']

    def __str__(self):
        """Return event's str representation."""
        return str(self.name)
