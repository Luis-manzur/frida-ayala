# Generated by Django 4.0.10 on 2023-05-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_alter_ticketeventday_ticket_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.TextField(default='Descripcion del ticket'),
            preserve_default=False,
        ),
    ]
