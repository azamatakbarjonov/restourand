# Generated by Django 5.1.7 on 2025-04-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='image',
            field=models.ImageField(default=1, upload_to='about/'),
            preserve_default=False,
        ),
    ]
