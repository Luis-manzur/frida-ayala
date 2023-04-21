"""Orders Models"""

# Utils
import uuid

# Django
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Models
from frida_ayala.events.models import Event
from frida_ayala.events.models.shows import EventDay
# Utilities
from frida_ayala.utils.models import FAModel


class Order(FAModel):
    tickets = models.ManyToManyField('tickets.Ticket', through='OrderTicket')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    event_day = ChainedForeignKey(
        EventDay,
        chained_field="event",
        chained_model_field="event",
        show_all=False,
        auto_choose=True,
        on_delete=models.SET_NULL, null=True
    )
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='order')
    code = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
