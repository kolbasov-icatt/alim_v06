# Generated by Django 5.0.3 on 2024-04-03 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_product_frequency_remove_product_growthrate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConsumptionData',
        ),
    ]
