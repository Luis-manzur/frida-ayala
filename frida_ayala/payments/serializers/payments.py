"""Payment serializer"""
import requests
# Django
from django.conf import settings
from django.http import JsonResponse
# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.payments.models import Payment


def make_payment(data):
    url = settings.INTERNATIONAL_CARDS_URL
    api_key = settings.INTERNATIONAL_API_KEY
    payment_data = {
        'monto': data['amount'],
        'cvc': data['cvc'],
        'mes': data['month'],
        'ano': data['year'],
        'numero': data['card'],
        'reference': data['reference']
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=payment_data, headers=headers)

    if response.status_code == 200:
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return False


class PaymentCreateSerializer(serializers.Serializer):
    YEAR_CHOICES = [
        ('40', '40'),
        ('39', '39'),
        ('38', '38'),
        ('37', '37'),
        ('36', '36'),
        ('35', '35'),
        ('34', '34'),
        ('33', '33'),
        ('32', '32'),
        ('31', '31'),
        ('30', '30'),
        ('29', '29'),
        ('28', '28'),
        ('27', '27'),
        ('26', '26'),
        ('25', '25'),
        ('24', '24'),
        ('23', '23'),
    ]
    MONTH_CHOICES = [
        ('12', '12'),
        ('11', '11'),
        ('10', '10'),
        ('09', '09'),
        ('08', '08'),
        ('07', '07'),
        ('06', '06'),
        ('05', '05'),
        ('04', '04'),
        ('03', '03'),
        ('02', '02'),
        ('01', '01'),
    ]
    card = serializers.CharField(max_length=16)
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    cvc = serializers.CharField(min_length=3, max_length=4)
    year = serializers.ChoiceField(choices=YEAR_CHOICES)
    month = serializers.ChoiceField(choices=MONTH_CHOICES)
    reference = serializers.IntegerField()

    def validate(self, obj):
        if settings.DEBUG:
            transaction_response = make_payment(obj)
            if not transaction_response:
                raise serializers.ValidationError("Transaction error, try again later.")
            data = {
                'card': obj['card'][-4:],
                'reference': transaction_response['referencia'],
                'amount': obj['amount'],
                'status': 'A' if transaction_response['ok'] else 'F',
                'code': transaction_response['codigo']
            }

            payment = Payment.objects.create(**data)
            payment.save()
            if transaction_response['ok']:
                return obj
            else:
                raise serializers.ValidationError(transaction_response['respuesta_data'])
        return obj
