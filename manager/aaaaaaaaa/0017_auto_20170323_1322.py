# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_equip_delivery_record_back_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equip_delivery_record',
            name='equip_type',
        ),
        migrations.AddField(
            model_name='equip_delivery_record',
            name='back_equip_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='寄回设备类型', to='manager.equip_type'),
        ),
        migrations.AddField(
            model_name='equip_delivery_record',
            name='send_equip_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='寄出设备类型', to='manager.equip_type'),
        ),
    ]