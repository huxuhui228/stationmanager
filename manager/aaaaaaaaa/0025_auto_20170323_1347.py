# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0024_auto_20170323_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip_delivery_record',
            name='note',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]
