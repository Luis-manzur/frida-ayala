"""Orders Models"""

# Utils
import uuid

# Django
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from frida_ayala.events.models import Event
from frida_ayala.events.models.shows import EventDay
# Models
from frida_ayala.tickets.models.tickets import Ticket
from frida_ayala.users.models import User
# Utilities
from frida_ayala.utils.models import FAModel


class Order(FAModel):
    tickets = models.ManyToManyField(Ticket, through='OrderTicket')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    event_day = ChainedForeignKey(
        EventDay,
        chained_field="event",
        chained_model_field="event",
        show_all=False,
        auto_choose=True,
        on_delete=models.SET_NULL, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
