# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_equip_delivery_record_back_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip_delivery_record',
            name='back_sender',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
