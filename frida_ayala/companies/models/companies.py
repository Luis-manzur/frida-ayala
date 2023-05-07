"""Companies models"""

# Django
from django.core.validators import RegexValidator
from django.db import models

# Utilities
from frida_ayala.utils.models import FAModel


class Company(FAModel):
    SECTORS = [
        ('T', 'Technology'),
        ('S', 'Services'),
        ('C', 'Commerce'),
        ('H', 'Health'),
        ('E', 'Education'),
        ('F', 'Food')

    ]
    name = models.CharField(max_length=100, unique=True)
    sector = models.CharField(choices=SECTORS, default='O', max_length=1)

    rif_regex = RegexValidator(
        regex=r'^[JG][-]\d{8}[-]\d$',
        message='The RIF number must be entered in the format: J12345678901. Up to 10 digits allowed.'
    )
    rif = models.CharField(max_length=13, validators=[rif_regex])
    logo = models.ImageField(upload_to='logos/', help_text='The image MUST NOT have background.')

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
