"""Payment models"""
# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Payment(FAModel):
    STATUS = [
        ('A', 'Approved'),
        ('R', 'Rejected'),
        ('P', 'Pending')
    ]

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS, default='P')
    reference = models.CharField(null=True, max_length=6)
    transaction_code = models.CharField(max_length=10, null=True)
    dni = models.CharField(max_length=10)
    order_id = models.UUIDField()
    response_data = models.JSONField(null=True)
    operating_system = models.CharField(max_length=16)
    os_version = models.CharField(max_length=16)
    origin_url = models.URLField()
    client_ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=16)
    browser_version = models.CharField(max_length=16)
    request_data = models.JSONField()
