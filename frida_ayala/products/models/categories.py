"""Category model"""

# Django
from django.db import models

# Utils
from frida_ayala.utils.models import FAModel


class Category(FAModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
