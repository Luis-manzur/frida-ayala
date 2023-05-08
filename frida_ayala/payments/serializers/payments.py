"""Payment serializer"""
import requests
# Django
from django.conf import settings
# Django REST Framework
from rest_framework import serializers


def make_payment(data):
    url = settings.INTERNATIONAL_CARDS_URL
    api_key = settings.INTERNATIONAL_API_KEY
    payment_data = {
        'monto': data['amount'],
        'cvc': data['cvc'],
        'mes': data['month'],
        'ano': data['year'],
        'numero': data['card'],
        'referencia': 95
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'apikey': api_key}
    response = requests.post(url, data=payment_data, headers=headers)

    if response.status_code == 200:
        if response.status_code == 200:
            data = response.json()
            return data
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
