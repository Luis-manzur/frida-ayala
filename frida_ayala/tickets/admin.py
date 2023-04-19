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
    list_filter = ('event__name',)
    search_fields = ('type', 'price', 'event')


class EventInline(admin.TabularInline):
    model = Event


class OrderTicketInline(admin.TabularInline):
    model = OrderTicket
    fk = 'order'
    exclude = ['entries']

    def get_can_delete(self, request, obj=None):
        if obj:
            return False
        else:
            return True

    def get_extra(self, request, obj=None):
        if obj:
            return 0
        else:
            return 3

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('ticket', 'first_name', 'last_name')
        else:
            return ()


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderTicketInline]
    list_display = ('code', 'user', 'created')
    list_filter = ('created',)
    search_fields = ('code', 'user')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('event', 'event_day', 'user', 'code')
        else:
            return ()

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            return TicketOrderForm
        else:
            return super().get_form(request, obj, **kwargs)

    class Media:
        js = (
            'js/ticket-category.js',
            'https://code.jquery.com/jquery-3.3.1.min.js'
        )


admin_site.register(Order, OrderAdmin)
admin_site.register(Ticket, TicketAdmin)
