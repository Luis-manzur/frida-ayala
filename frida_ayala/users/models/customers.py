"""Customer Model"""
# Django
from django.core.validators import RegexValidator
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Customer(FAModel):
    """Profile model.
    A profile holds a user's public data.
    """
    GENDERS = [
        ('F', 'Feminine'),
        ('M', 'Masculine'),
        ('O', 'Other')
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(
        'email address'
    )

    ci_regex = RegexValidator(
        regex=r'^[V|E][-]\d{8}$',
        message='The CI number must be entered in the format: V12345678901. Up to 10 digits allowed.'
    )
    ci = models.CharField(max_length=12, validators=[ci_regex])

    gender = models.CharField(max_length=1, choices=GENDERS, default='O')
    address = models.CharField(max_length=60)
    order = models.OneToOneField('tickets.Order', related_name='customer', on_delete=models.CASCADE)

    def __str__(self):
        """Return user's str representation."""
        return str(f'{self.first_name} {self.last_name}')
