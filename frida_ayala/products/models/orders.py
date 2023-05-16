"""Order models"""

# Utils
import uuid

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class ProductOrder(FAModel):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('X', 'Cancelled'),
    )

    PAYMENT_CHOICES = (
        ('CARD', 'Debit/Credit card'),
        ('CASH', 'Cash'),
    )

    SHIPPING_CHOICES = (
        ('DELIVERY', 'Delivery'),
        ('MRW', 'MRW'),
    )
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField('products.Product', through='OrderItem')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    code = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    shipping = models.ForeignKey('locations.Shipping', related_name='orders', on_delete=models.CASCADE, null=True)
    delivery = models.ForeignKey('locations.Delivery', related_name='orders', on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default="CARD")
    shipping_method = models.CharField(max_length=10, choices=SHIPPING_CHOICES, default="DELIVERY")

    def __str__(self):
        return f"Order #{self.code} ({self.status})"
