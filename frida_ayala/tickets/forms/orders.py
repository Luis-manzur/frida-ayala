"""Orders form"""

# Django
from django import forms

# Models
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.orders_tickets import OrderTicket


# Tasks


class OrderTicketForm(forms.ModelForm):
    class Meta:
        model = OrderTicket
        fields = '__all__'


class TicketOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['code', 'tickets', 'user']
