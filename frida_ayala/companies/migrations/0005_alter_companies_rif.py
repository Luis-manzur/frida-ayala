# Generated by Django 4.0.10 on 2023-04-19 01:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_remove_companies_contact_contact_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='rif',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='The CI number must be entered in the format: J12345678901. Up to 10 digits allowed.', regex='/^[J|G]\\d{8,10}$/i')]),
        ),
    ]