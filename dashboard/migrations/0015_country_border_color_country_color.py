# Generated by Django 5.0.3 on 2024-04-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_foodcat_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='border_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
