"""Ticket signals"""

from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from frida_ayala.tickets.models import Order
# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email_user


@receiver(post_save, sender=Order)
def send_order_email(sender, instance: Order, created, **kwargs):
    if created:
        if instance.user:
            send_ticket_purchase_email_user.delay(instance.pk)
