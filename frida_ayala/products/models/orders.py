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
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField('products.Product', through='OrderItem')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    code = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    shipping = models.ForeignKey('locations.Shipping', related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.code} ({self.status})"
