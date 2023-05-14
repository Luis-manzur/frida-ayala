"""Sizes models"""

# Django
from django.db import models

# Utils
from frida_ayala.utils.models import FAModel


class Size(FAModel):
    name = models.CharField(max_length=50)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name
