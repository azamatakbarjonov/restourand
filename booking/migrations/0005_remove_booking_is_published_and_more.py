# Generated by Django 5.2 on 2025-05-17 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_booking_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='update_date',
        ),
    ]
