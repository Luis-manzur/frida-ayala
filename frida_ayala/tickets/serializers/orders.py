"""Ticket orders"""
import logging

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
from frida_ayala.tickets.tasks import send_ticket_purchase_email_user

logger = logging.getLogger('console')


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

        send_ticket_purchase_email_user.delay(data['user'].pk)
        return order


class OrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tickets = TicketOrderModelSerializer(many=True, read_only=True, source='orderticket_set')

    class Meta:
        model = Order
        exclude = ['created', 'modified']


class VerifyTicketSerializer(serializers.Serializer):
    token = serializers.UUIDField()

    def validate_token(self, data):
        error = None
        try:
            order_ticket: OrderTicket = OrderTicket.objects.get(code=data)
            if not order_ticket.active:
                error = 'Este ticket ya fue utilizado.'
                raise Exception('Ticket already used')
            self.context['order_ticket'] = order_ticket
        except Exception as e:
            if not error:
                error = 'Ticket no encontrado'
            logger.info(f'error validating in VerifyTicketSerializer: {e}')
            raise serializers.ValidationError(error)

        return data

    def create(self, data):
        try:
            order_ticket: OrderTicket = self.context['order_ticket']
            order_ticket.entries -= 1
            if order_ticket.entries <= 0:
                order_ticket.active = False
            order_ticket.save()
            return order_ticket
        except Exception as e:
            logger.info(f'error saving in VerifyTicketSerializer: {e}')
            raise serializers.ValidationError('Error desconocido intente de nuevo')
