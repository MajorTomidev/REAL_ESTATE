# Generated by Django 4.1.7 on 2023-02-21 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestateapp', '0009_companydetails_comapany_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydetails',
            old_name='comapany_location',
            new_name='company_location',
        ),
    ]
