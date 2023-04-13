"""Movies models."""

# Django
from django.db import models

# Models
from frida_ayala.events.models.shows import EventDay
# Utilities
from frida_ayala.utils.models import FAModel


class Movie(FAModel):
    """Movie model."""
    name = models.CharField('Movie name', max_length=120)
    slug_name = models.SlugField(unique=True, max_length=40)
    banner = models.ImageField(upload_to='movies/banners', unique=True)
    duration = models.DurationField()
    about = models.CharField('Movie description', max_length=255)
    show = models.ForeignKey(EventDay, related_name='movie', null=True, on_delete=models.SET_NULL)
    trailer_url = models.URLField(max_length=200)

    class Meta:
        indexes = [
            models.Index(fields=['slug_name'])
        ]
        ordering = ['-created']

    def __str__(self):
        """Return movie's str representation."""
        return str(self.name)
