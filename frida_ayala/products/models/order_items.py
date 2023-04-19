"""Order items models"""

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class OrderItem(FAModel):
    order = models.ForeignKey('products.ProductOrder', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.order} - {self.product} x{self.quantity}"
