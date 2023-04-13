"""Orders Models"""

# Utils
import uuid

# Django
from django.db import models

# Models
from frida_ayala.tickets.models.tickets import TicketEventDay
from frida_ayala.users.models import User
# Utilities
from frida_ayala.utils.models import FAModel


class Order(FAModel):
    tickets = models.ManyToManyField(TicketEventDay, through='OrderTicket')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
