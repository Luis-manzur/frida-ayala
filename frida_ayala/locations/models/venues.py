"""Venues model."""

# Django
from django.core.validators import MinValueValidator
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Models
from frida_ayala.locations.models.municipalities import Municipality
from frida_ayala.locations.models.states import State
from frida_ayala.utils.models import FAModel


class Venue(FAModel):
    name = models.CharField(max_length=60)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    municipality = ChainedForeignKey(
        Municipality,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        """Return name str representation."""
        return str(self.name)
