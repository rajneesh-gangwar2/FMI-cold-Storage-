# Generated by Django 4.1 on 2022-08-30 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0005_enquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='email',
            new_name='emailaddress',
        ),
    ]
