"""Sponsors Models."""

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Sponsor(FAModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    arrangement = models.TextField()
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
