# Generated by Django 5.0.3 on 2024-04-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_food_slug_alter_food_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(max_length=70),
        ),
        migrations.AlterField(
            model_name='food',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
