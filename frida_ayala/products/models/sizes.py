"""Sizes models"""

# Django
from django.db import models

# Utils
from frida_ayala.utils.models import FAModel


class Size(FAModel):
    name = models.CharField(max_length=4)
    stock = models.IntegerField(default=1)
    product = models.ForeignKey('products.Product', related_name='sizes', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + ' (' + self.name + ')'
