"""Shippings model."""

from django.core.validators import RegexValidator
# Django
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Models
from frida_ayala.locations.models.municipalities import Municipality
from frida_ayala.locations.models.states import State
from frida_ayala.utils.models import FAModel


class Shipping(FAModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    municipality = ChainedForeignKey(
        Municipality,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        on_delete=models.CASCADE)
    office = models.CharField(max_length=60)

    postal_code_regex = RegexValidator(
        regex=r'^\d{4}$',
        message="Postal code must have 4 digits"
    )

    postal_code = models.CharField(max_length=4, validators=[postal_code_regex])

    def __str__(self):
        """Return name str representation."""
        return str(self.state.name + ' ' + self.municipality.name + ' ' + self.postal_code + ' ' + self.office)


class Delivery(FAModel):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address
