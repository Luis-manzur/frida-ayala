# Generated by Django 4.0.10 on 2023-04-19 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_sponsors'),
        ('tickets', '0005_ticket_entries'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('type', 'event')},
        ),
    ]
