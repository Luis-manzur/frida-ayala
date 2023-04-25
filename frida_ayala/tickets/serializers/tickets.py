"""Tickets serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.tickets.models import Ticket, TicketEventDay


class TicketSerializer(serializers.ModelSerializer):
    """Ticket model serializer"""
    stock_by_day = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        exclude = ['modified', 'created', 'event', 'stock']

    def get_stock_by_day(self, obj: Ticket):
        event_days = TicketEventDay.objects.filter(ticket_type=obj.pk)
        data = []
        for event_day in event_days:
            data.append({
                'event_day': event_day.event_day.pk,
                'stock': event_day.stock
            })
        return data
