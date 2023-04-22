# Generated by Django 4.0.10 on 2023-04-22 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_remove_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderticket',
            name='ci',
            field=models.CharField(default=1, max_length=12, validators=[django.core.validators.RegexValidator(message='The CI number must be entered in the format: V12345678901. Up to 10 digits allowed.', regex='^[V|E][-]\\d{8}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderticket',
            name='qr',
            field=models.ImageField(default=None, upload_to='qr/'),
            preserve_default=False,
        ),
    ]
