# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 01:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_equip_delivery_record_back_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equip_delivery_record',
            name='back_status',
        ),
    ]
