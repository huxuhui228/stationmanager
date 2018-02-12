# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_station_project_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='project_source',
            field=models.CharField(blank=True, choices=[('九五', '九五'), ('十五', '十五'), ('十一五', '十一五'), ('十二五', '十二五'), ('背景场', '背景场'), ('十三五', '十三五')], default='', max_length=32, null=True),
        ),
    ]
