# Generated by Django 5.0.3 on 2024-04-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_country_border_color_country_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='border_color',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='color',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
