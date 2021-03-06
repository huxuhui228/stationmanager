# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equip_maintain_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=64)),
                ('fault_startdate', models.DateTimeField(auto_now=True, null=True)),
                ('fault_enddate', models.DateTimeField(auto_now=True, null=True)),
                ('maintain_date', models.DateTimeField(auto_now=True, null=True)),
                ('staff', models.CharField(blank=True, max_length=32, null=True)),
                ('note', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': '设备维护记录',
                'verbose_name_plural': '设备维护记录',
            },
        ),
        migrations.CreateModel(
            name='equip_manu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('staff_name', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('note', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': '设备生产厂家',
                'verbose_name_plural': '设备生产厂家',
            },
        ),
        migrations.CreateModel(
            name='equip_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', '台上正常使用'), ('2', '在库'), ('3', '在修')], max_length=32)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('ip_mask', models.GenericIPAddressField(blank=True, default='255.255.255.0', null=True)),
                ('ip_gateway', models.GenericIPAddressField(blank=True, null=True)),
                ('sampling_rate', models.CharField(blank=True, choices=[('100sps', '每秒100点'), ('200sps', '每秒200点'), ('50sps', '每秒50点'), ('1spm', '每分1点'), ('1sph', '每小时1点')], max_length=32, null=True)),
                ('transmission_type', models.CharField(blank=True, choices=[('SDH', 'SDH'), ('3G', '3G'), ('Internet_VPN', 'Internet_VPN'), ('电台', '电台')], max_length=32, null=True)),
                ('install_date', models.DateTimeField(auto_now=True, null=True)),
                ('remove_date', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': '设备状态',
                'verbose_name_plural': '设备状态',
            },
        ),
        migrations.CreateModel(
            name='equip_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('measure_means', models.CharField(choices=[('cezhen', '测震'), ('qiangzhen', '强震'), ('xingbian', '形变'), ('liuti', '流体'), ('dianci', '电磁')], max_length=32)),
                ('note', models.CharField(blank=True, max_length=128, null=True)),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equip_manu')),
            ],
            options={
                'verbose_name': '设备类型',
                'verbose_name_plural': '设备类型',
            },
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(blank=True, max_length=64, null=True)),
                ('note', models.CharField(blank=True, max_length=128, null=True)),
                ('equip_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equip_type')),
            ],
            options={
                'verbose_name': '设备列表',
                'verbose_name_plural': '设备列表',
            },
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('name_en', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('name_cn', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('measure_means', models.CharField(blank=True, choices=[('cezhen', '测震'), ('qiangzhen', '强震'), ('xingbian', '形变'), ('liuti', '流体'), ('dianci', '电磁')], default='测震', max_length=32, null=True)),
                ('district', models.CharField(choices=[('济南', '济南'), ('泰安', '泰安'), ('潍坊', '潍坊'), ('德州', '德州'), ('滨州', '滨州'), ('莱芜', '莱芜'), ('青岛', '青岛'), ('烟台', '烟台'), ('日照', '日照'), ('东营', '东营'), ('济宁', '济宁'), ('荷泽', '荷泽'), ('聊城', '聊城'), ('临沂', '临沂'), ('枣庄', '枣庄'), ('淄博', '淄博'), ('威海', '威海'), ('省局', '省局')], default='济南', max_length=32)),
                ('longtitude', models.FloatField(blank=True, default=None, null=True)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('heigh', models.FloatField(blank=True, default=None, null=True)),
                ('lithology', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('staff_name', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('note', models.CharField(blank=True, default='', max_length=256, null=True)),
            ],
            options={
                'verbose_name': '台站列表',
                'verbose_name_plural': '台站列表',
            },
        ),
        migrations.AddField(
            model_name='equip_status',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equipment'),
        ),
        migrations.AddField(
            model_name='equip_status',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.station'),
        ),
        migrations.AddField(
            model_name='equip_maintain_record',
            name='equip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equipment'),
        ),
    ]
