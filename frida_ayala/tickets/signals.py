"""Ticket signals"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from frida_ayala.events.models import EventDay
# Models
from frida_ayala.tickets.models import Order, Ticket, TicketEventDay
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email_user


@receiver(post_save, sender=Order)
def send_order_email(sender, instance: Order, created, **kwargs):
    if created:
        if instance.user:
            send_ticket_purchase_email_user.delay(instance.pk)


@receiver(post_save, sender=Ticket)
def create_stock_for_days(sender, instance: Ticket, created, **kwargs):
    if created:
        event_days = EventDay.objects.filter(event=instance.event)
        for event_day in event_days:
            TicketEventDay.objects.create(ticket_type=instance, event_day=event_day, stock=instance.stock).save()
