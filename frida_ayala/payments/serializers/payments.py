"""Payment serializer"""
import requests
# Django
from django.conf import settings
# Django REST Framework
from rest_framework import serializers

# Model
from frida_ayala.payments.models import Payment
# Operations
from frida_ayala.utils.operations import generate_reference_number


def make_payment(data):
    url = settings.INTERNATIONAL_CARDS_URL + '/sandbox/init/' + settings.INTERNATIONAL_CARDS_URL
    api_key = settings.INTERNATIONAL_API_KEY
    payment_data = {
        'Monto': str(data['amount']),
        'Dni': data['dni'],
        'Name': data['name'],
        'Ref': generate_reference_number(),
        'Urldone': settings.INTERNATIONAL_PAYMENT_DONDE_URL,
        'Urlcancel': settings.INTERNATIONAL_PAYMENT_CANCEL_URL,
        'Externalid': settings.EXTERNAL_ID,
        'Descripcion': 'Pago en tienda'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': f'Bearer {api_key}'}
    response = requests.post(url, data=payment_data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data, payment_data
    else:
        return False


class PaymentCreateSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=16)
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    name = serializers.CharField(max_length=32)


class PaymentModelSerializer(serializers.ModelSerializer):
    """Payment Model serializer"""

    class Meta:
        model = Payment
        exclude = ['modified', 'created']
