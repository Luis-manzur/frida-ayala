"""Stands Models"""

from django.core.validators import RegexValidator
# Django
from django.db import models

# Models
# Utilities
from frida_ayala.utils.models import FAModel


class Stands(FAModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    arrangement = models.TextField()

    zone_regex = RegexValidator(
        regex='^[A-Z][0-9]$',
        message='Zone code must be a code with a maximum length of 2  characters where the first is a Capital letter '
                'and second is number Example: A1'
    )
    zone = models.CharField(max_length=2, help_text='Zone must be unique by event', validators=[zone_regex])
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('zone', 'event')
