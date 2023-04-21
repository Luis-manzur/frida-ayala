"""Ticket signals"""

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Tasks
from frida_ayala.tickets.tasks import send_ticket_purchase_email_customer
# Models
from frida_ayala.users.models import Customer


@receiver(post_save, sender=Customer)
def send_order_email(sender, instance: Customer, created, **kwargs):
    if created:
        send_ticket_purchase_email_customer.delay(instance.pk)
