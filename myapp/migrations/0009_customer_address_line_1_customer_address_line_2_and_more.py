# Generated by Django 4.2.3 on 2023-07-08 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address_line_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='post_code',
            field=models.CharField(default='', max_length=5, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{4,5}$')]),
        ),
    ]