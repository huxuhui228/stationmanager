# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20170317_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip_delivery_record',
            name='receiver_unit',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]