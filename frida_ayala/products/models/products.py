"""Products Models"""

# Django
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Product(FAModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='The amount MUST be given in USD')
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    supplier = models.ForeignKey('companies.Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
