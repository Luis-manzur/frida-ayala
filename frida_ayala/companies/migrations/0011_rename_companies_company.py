# Generated by Django 4.0.10 on 2023-04-24 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_itinerary'),
        ('products', '0002_product_stock'),
        ('companies', '0010_alter_contact_ci'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companies',
            new_name='Company',
        ),
    ]
