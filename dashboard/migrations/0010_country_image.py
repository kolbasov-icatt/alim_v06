# Generated by Django 5.0.3 on 2024-04-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_area_country_alter_frequency_times_per_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
