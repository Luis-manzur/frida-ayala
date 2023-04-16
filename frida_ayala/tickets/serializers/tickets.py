"""Tickets serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    """Ticket model serializer"""

    class Meta:
        model = Ticket
        exclude = ['modified', 'created', 'event', 'stock']
