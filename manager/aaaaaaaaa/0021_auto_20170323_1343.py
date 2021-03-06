# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_auto_20170323_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip_delivery_record',
            name='back_equip_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='寄回设备类型', to='manager.equip_type', verbose_name='寄回设备类型'),
        ),
        migrations.AlterField(
            model_name='equip_delivery_record',
            name='back_sender',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='寄回人'),
        ),
        migrations.AlterField(
            model_name='equip_delivery_record',
            name='back_unit',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='寄回单位'),
        ),
    ]
