"""Celery tasks."""

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from frida_ayala.tickets.models import Order, OrderTicket


@shared_task()
def send_ticket_purchase_email(user_pk):
    order = Order.objects.filter(user=user_pk).first()
    ticket_orders = OrderTicket.objects.filter(order=order)
    tickets = order.tickets.all()
    total = 0
    for ticket in tickets: total += ticket.price

    user = order.user
    subject = f'Entradas {order.event.name}'
    from_email = settings.DEFAULT_FROM_EMAIL
    content = render_to_string(
        'emails/tickets/qr.html',
        {'tickets': tickets, 'user': user, 'ticket_orders': ticket_orders, 'order': order, 'total': total},
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, 'text/html')
    msg.send()
