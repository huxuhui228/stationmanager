# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20170310_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip_manu',
            name='emai_address',
            field=models.EmailField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='equip_manu',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='equip_type',
            name='manufacture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.equip_manu'),
        ),
        migrations.AlterField(
            model_name='equip_type',
            name='measure_means',
            field=models.CharField(blank=True, choices=[('cezhen', '测震'), ('qiangzhen', '强震'), ('xingbian', '形变'), ('liuti', '流体'), ('dianci', '电磁')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='equip_type',
            name='model',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='equip_type',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='district',
            field=models.CharField(choices=[('济南', '济南'), ('泰安', '泰安'), ('潍坊', '潍坊'), ('德州', '德州'), ('滨州', '滨州'), ('莱芜', '莱芜'), ('青岛', '青岛'), ('烟台', '烟台'), ('日照', '日照'), ('东营', '东营'), ('济宁', '济宁'), ('菏泽', '菏泽'), ('聊城', '聊城'), ('临沂', '临沂'), ('枣庄', '枣庄'), ('淄博', '淄博'), ('威海', '威海'), ('省局', '省局')], default='济南', max_length=32),
        ),
        migrations.AlterField(
            model_name='station',
            name='measure_means',
            field=models.CharField(blank=True, choices=[('cezhen', '测震'), ('qiangzhen', '强震'), ('qianzhao', '前兆')], default='测震', max_length=32, null=True),
        ),
    ]
