"""Ticket orders"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.events.models.events import Event
from frida_ayala.events.models.shows import EventDay
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.orders_tickets import OrderTicket
# Serializers
from frida_ayala.tickets.serializers.ticket_orders import TicketOrderModelSerializer, TicketOrderCreateModelSerializer
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email


class OrderCreateSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tickets = serializers.ListField(child=TicketOrderCreateModelSerializer())
    event = serializers.SlugRelatedField(slug_field='slug_name', queryset=Event.objects.all())
    event_day = serializers.PrimaryKeyRelatedField(queryset=EventDay.objects.all())

    def create(self, data):
        tickets_data = data.pop('tickets')

        order = Order(**data)
        order.save()
        for ticket_data in tickets_data:
            ticket_data['order'] = order
            ticket = OrderTicket.objects.create(**ticket_data)
            ticket.save()

        send_ticket_purchase_email.delay(data['user'].pk)
        return order


class OrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tickets = TicketOrderModelSerializer(many=True, read_only=True, source='orderticket_set')

    class Meta:
        model = Order
        exclude = ['created', 'modified']
