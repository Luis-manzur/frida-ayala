"""Orders form"""

# Django
from django import forms
# Smart selects
from smart_selects.form_fields import ChainedModelChoiceField

# Models
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.orders_tickets import OrderTicket
from frida_ayala.tickets.models.tickets import Ticket
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email


class OrderTicketForm(forms.ModelForm):

    class Meta:
        model = OrderTicket
        fields = '__all__'


class TicketOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ['code']

    def save(self, commit=True):
        order = super(TicketOrderForm, self).save(commit)
        send_ticket_purchase_email.delay(self.cleaned_data['user'].pk)
        return order
