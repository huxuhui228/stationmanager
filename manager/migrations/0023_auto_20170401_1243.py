# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0022_auto_20170401_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='to_do_time',
            field=models.DateField(blank=True, null=True, verbose_name='计划处理时间'),
        ),
    ]