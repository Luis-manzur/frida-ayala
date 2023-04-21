"""Payment models"""
# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Payment(FAModel):
    STATUS = [
        ('A', 'Aprobado'),
        ('F', 'Fallido')
    ]
    card = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    code = models.CharField(max_length=36)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    reference = models.IntegerField()
