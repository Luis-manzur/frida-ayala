"""Celery tasks."""
# utils
from io import BytesIO

import qrcode
# Celery
from celery import shared_task
from django.conf import settings
# Django
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Models
from frida_ayala.tickets.models import OrderTicket, Order
from frida_ayala.users.models import Customer


def common_email_settings(order, user):
    ticket_orders = OrderTicket.objects.filter(order=order)
    tickets = order.tickets.all()
    total = 0
    for ticket in ticket_orders:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        data = ticket.code
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        image_file = ContentFile(buffer.getvalue())
        qr_code_file = File(image_file)
        qr_code_file.name = 'my_qr_code.png'
        ticket.qr = qr_code_file
        ticket.save()
        total += ticket.ticket.price
    subject = f'Entradas {order.event.name}'
    from_email = settings.DEFAULT_FROM_EMAIL
    content = render_to_string(
        'emails/tickets/qr.html',
        {'tickets': tickets, 'user': user, 'ticket_orders': ticket_orders, 'order': order, 'total': total},
    )

    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, 'text/html')
    msg.send()


@shared_task()
def send_ticket_purchase_email_customer(customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    order = customer.order
    common_email_settings(order, customer)


@shared_task()
def send_ticket_purchase_email_user(order_code):
    order = Order.objects.get(code=order_code)
    user = order.user
    common_email_settings(order, user)
