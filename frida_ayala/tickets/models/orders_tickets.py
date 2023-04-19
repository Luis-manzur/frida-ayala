"""OrderTicket many-to-many model"""

# Utils
import uuid

# Django
from django.db import models

# Models
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.tickets import Ticket
# Utilities
from frida_ayala.utils.models import FAModel


class OrderTicket(FAModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    entries = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.entries = self.ticket.entries
        super().save(*args, **kwargs)
