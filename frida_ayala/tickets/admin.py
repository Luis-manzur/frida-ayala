"""Tickets admin panel"""
from django.contrib import admin

# Django
from frida_ayala.events.models import Event
# Forms
from frida_ayala.tickets.forms.orders import TicketOrderForm
# models
from frida_ayala.tickets.models.orders import Order
from frida_ayala.tickets.models.orders_tickets import OrderTicket
from frida_ayala.tickets.models.tickets import Ticket
from frida_ayala.utils.admin import admin_site


class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type', 'event', 'price')
    list_filter = ('event',)
    search_fields = ('type', 'price', 'event')


class EventInline(admin.TabularInline):
    model = Event


class OrderTicketInline(admin.TabularInline):
    model = OrderTicket
    inlines = [EventInline]
    fk = 'order'


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderTicketInline]
    form = TicketOrderForm
    list_display = ('code', 'user', 'created')
    list_filter = ('created',)
    search_fields = ('code', 'user')

    class Media:
        js = (
            'js/ticket-category.js',
            'https://code.jquery.com/jquery-3.3.1.min.js'
        )


admin_site.register(Order, OrderAdmin)
admin_site.register(Ticket, TicketAdmin)
