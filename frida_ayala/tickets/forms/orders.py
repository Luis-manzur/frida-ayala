"""Orders form"""

# Django
from django import forms
# Smart selects
from smart_selects.form_fields import ChainedModelChoiceField

# Models
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.orders_tickets import OrderTicket
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email


class OrderTicketForm(forms.ModelForm):
    # ticket = ChainedModelChoiceField(
    #     queryset=Ticket.objects.all(),
    #     chained_field='event',
    #     chained_model_field='order',
    #     show_all=True,
    #     auto_choose=True,
    #     to_app_name='tickets',
    #     to_model_name='OrderTicket',
    #     foreign_key_app_name='tickets',
    #     foreign_key_model_name='Order',
    #     foreign_key_field_name='event'
    # )

    class Meta:
        model = OrderTicket
        fields = '__all__'


class TicketOrderForm(forms.ModelForm):
    ticket = OrderTicketForm()

    class Meta:
        model = Order
        exclude = ['code']

    def save(self, commit=True):
        order = super(TicketOrderForm, self).save(commit)
        send_ticket_purchase_email.delay(self.cleaned_data['user'].pk)
        return order
