# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Cart(FAModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Size', through='CartItem')


class CartItem(FAModel):
    size = models.ForeignKey('products.Size', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
