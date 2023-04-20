"""Orders form"""

# Django
from django import forms

# Models
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.orders_tickets import OrderTicket
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email


# Smart selects


class OrderTicketForm(forms.ModelForm):
    class Meta:
        model = OrderTicket
        fields = '__all__'


class TicketOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['code', 'tickets', 'customer']

    def save(self, commit=True):
        order = super(TicketOrderForm, self).save(commit)
        send_ticket_purchase_email.delay(self.cleaned_data['user'].pk)
        return order
