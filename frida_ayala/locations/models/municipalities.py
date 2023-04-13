"""Municipalities model."""

# Django
from django.db import models

# Models
from frida_ayala.locations.models.states import State


class Municipality(models.Model):
    name = models.CharField(max_length=60)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        """Return name str representation."""
        return str(self.name)
