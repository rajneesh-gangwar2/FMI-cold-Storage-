# Generated by Django 4.1 on 2022-08-29 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0002_merchantinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchantinfo',
            old_name='firname',
            new_name='firmname',
        ),
    ]
