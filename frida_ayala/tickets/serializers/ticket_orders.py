"""Ticket orders Serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.tickets.models.orders_tickets import OrderTicket
# Serializers
from frida_ayala.tickets.serializers.tickets import TicketSerializer


class TicketOrderCreateModelSerializer(serializers.ModelSerializer):
    """Ticket Order Model Serializer"""

    class Meta:
        model = OrderTicket
        exclude = ['created', 'modified', 'order', 'active', 'entries']


class TicketOrderModelSerializer(serializers.ModelSerializer):
    """Ticket Order Model Serializer"""
    ticket = TicketSerializer(read_only=True)

    class Meta:
        model = OrderTicket
        exclude = ['created', 'modified', 'order', 'active']
