"""Sponsors Models."""

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Sponsors(FAModel):
    company = models.ForeignKey('companies.Companies', on_delete=models.CASCADE)
    arrangement = models.TextField()
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
