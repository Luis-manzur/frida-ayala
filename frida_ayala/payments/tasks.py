"""Celery tasks."""
# utils
import requests
# Celery
from celery import shared_task
# Django
from django.conf import settings

# Models
from frida_ayala.payments.models import Payment


@shared_task()
def update_pending_payment(payment_id):

    STATUS = {
        'approved': 'A',
        'rejected': 'R',
        'pending': 'P'
    }

    payment = Payment.objects.get(id=payment_id)
    url = settings.INTERNATIONAL_CARDS_URL + '/sandbox/orden/' + str(payment.order_id)
    api_key = settings.INTERNATIONAL_API_KEY
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    data = response_data['data']

    payment.response_data = response_data
    payment.reference = data['Ref']
    status = STATUS[data['Status']]
    payment.status = STATUS[data['Status']]
    if status == 'P':
        payment.status = 'R'
    payment.save()

@shared_task()
def update_pending_payments():
    STATUS = {
        'approved': 'A',
        'rejected': 'R',
        'pending': 'P'
    }
    pending_payments = Payment.objects.filter(status='P')
    if pending_payments:
        for i in pending_payments:
            i: Payment = i
            url = settings.INTERNATIONAL_CARDS_URL + '/sandbox/orden/' + str(i.order_id)
            api_key = settings.INTERNATIONAL_API_KEY
            headers = {'Authorization': f'Bearer {api_key}'}
            response = requests.get(url, headers=headers)
            response_data = response.json()
            data = response_data['data']
            print(data)
            i.response_data = response_data
            i.reference = data['Ref']
            i.status = STATUS[data['Status']]
            i.save()
