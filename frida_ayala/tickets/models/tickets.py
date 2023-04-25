"""Tickets models"""

from django.core.validators import MinValueValidator, MaxValueValidator
# Django
from django.db import models

# Models
from frida_ayala.events.models import Event
from frida_ayala.events.models.shows import EventDay
# Utilities
from frida_ayala.utils.models import FAModel
from frida_ayala.utils.validators import validate_price_amount, validate_ticket_stock


class Ticket(FAModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_price_amount])
    entries = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    stock = models.IntegerField(validators=[validate_ticket_stock])

    class Meta:
        unique_together = ('type', 'event')

    def __str__(self):
        return self.type


class TicketEventDay(FAModel):
    ticket_type = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='event_days')
    event_day = models.ForeignKey(EventDay, on_delete=models.CASCADE)
    stock = models.IntegerField(validators=[validate_ticket_stock])
