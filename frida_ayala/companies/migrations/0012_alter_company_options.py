# Generated by Django 4.0.10 on 2023-05-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_rename_companies_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
    ]
