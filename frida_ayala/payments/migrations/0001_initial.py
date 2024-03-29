# Generated by Django 4.0.10 on 2023-04-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('card', models.CharField(max_length=4)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('code', models.CharField(max_length=36)),
                ('status', models.CharField(choices=[('A', 'Aprobado'), ('F', 'Fallido')], default='A', max_length=1)),
                ('reference', models.IntegerField()),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
