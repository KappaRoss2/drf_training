# Generated by Django 3.2 on 2022-11-19 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='category',
            new_name='cat',
        ),
    ]
