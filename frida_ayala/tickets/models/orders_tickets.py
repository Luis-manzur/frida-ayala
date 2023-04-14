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
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
