# Generated by Django 4.1.7 on 2023-02-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestateapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='house_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_zipcode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
