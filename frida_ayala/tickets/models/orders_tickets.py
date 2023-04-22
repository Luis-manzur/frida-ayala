"""OrderTicket many-to-many model"""

# Utils
import uuid

# QR
# Django
from django.core.validators import RegexValidator
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class OrderTicket(FAModel):
    order = models.ForeignKey('tickets.Order', on_delete=models.CASCADE)
    ticket = models.ForeignKey('tickets.Ticket', on_delete=models.CASCADE)
    ci_regex = RegexValidator(
        regex=r'^[V|E][-]\d{8}$',
        message='The CI number must be entered in the format: V12345678901. Up to 10 digits allowed.'
    )
    ci = models.CharField(max_length=12, validators=[ci_regex])
    active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    entries = models.IntegerField(default=1)
    qr = models.ImageField(upload_to='qr/')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.entries = self.ticket.entries
        super().save(*args, **kwargs)
