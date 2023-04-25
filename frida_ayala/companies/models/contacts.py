"""Contacts models"""

# Django
from django.core.validators import RegexValidator
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Contact(FAModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    ci_regex = RegexValidator(
        regex=r'^[V|E][-]\d{8}$',
        message='The CI number must be entered in the format: V12345678901. Up to 10 digits allowed.'
    )
    ci = models.CharField(max_length=12, validators=[ci_regex])

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    position = models.CharField(max_length=20)
    company = models.OneToOneField('companies.Company', on_delete=models.CASCADE, related_name='contact')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
