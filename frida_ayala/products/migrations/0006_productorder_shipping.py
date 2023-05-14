# Generated by Django 4.0.10 on 2023-05-14 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_shipping'),
        ('products', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='shipping',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='locations.shipping'),
            preserve_default=False,
        ),
    ]
