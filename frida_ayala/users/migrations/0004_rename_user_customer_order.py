# Generated by Django 4.0.10 on 2023-04-20 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='order',
        ),
    ]