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
from frida_ayala.users.models import Customer
# Utils
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
    exclude = ['entries', 'qr']

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


class CustomerInline(admin.StackedInline):
    model = Customer
    verbose_name = 'Customer'
    verbose_name_plural = 'Customer'


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderTicketInline, CustomerInline]
    list_display = ('code', 'user', 'customer', 'created')
    list_filter = ('created',)
    search_fields = ('code', 'user')

    def customer(self, obj: Order):
        return obj.customer

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

    def get_inlines(self, request, obj: Order):
        if obj and obj.user:
            return [OrderTicketInline]
        return [CustomerInline, OrderTicketInline]

    class Media:
        js = (
            'js/ticket-category.js',
        )


admin_site.register(Order, OrderAdmin)
admin_site.register(Ticket, TicketAdmin)
