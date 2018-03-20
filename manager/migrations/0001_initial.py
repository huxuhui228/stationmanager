# Generated by Django 2.0 on 2018-03-20 07:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, default='', max_length=32)),
            ],
            options={
                'verbose_name': 'district',
            },
        ),
        migrations.CreateModel(
            name='equip_delivery_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(blank=True, default='', max_length=64, verbose_name='序列号')),
                ('number', models.IntegerField(blank=True, default=1, null=True, verbose_name='寄出数量')),
                ('send_date', models.DateField(blank=True, null=True, verbose_name='发件时间')),
                ('sender', models.CharField(blank=True, choices=[('胡旭辉', '胡旭辉'), ('李小晗', '李小晗'), ('王杰民', '王杰民'), ('曲利', '曲利'), ('冯志军', '冯志军'), ('马丕峰', '马丕峰'), ('王忠民', '王忠民'), ('吴双', '吴双')], max_length=32, verbose_name='发件人')),
                ('receiver_unit', models.CharField(blank=True, max_length=32, verbose_name='收件单位')),
                ('receiver', models.CharField(blank=True, max_length=32, verbose_name='收件人')),
                ('back_status', models.CharField(blank=True, choices=[('未返回', '未返回'), ('已返回', '已返回'), ('部分返回', '部分返回'), ('无需返回', '无需返回')], default='未返回', max_length=32, verbose_name='返回状态')),
                ('back_serial_num', models.CharField(blank=True, max_length=64, verbose_name='寄回序列号')),
                ('back_unit', models.CharField(blank=True, max_length=32, verbose_name='寄回单位')),
                ('back_sender', models.CharField(blank=True, max_length=32, verbose_name='寄回人')),
                ('back_receiver', models.CharField(blank=True, choices=[('胡旭辉', '胡旭辉'), ('李小晗', '李小晗'), ('王杰民', '王杰民'), ('曲利', '曲利'), ('冯志军', '冯志军'), ('马丕峰', '马丕峰'), ('王忠民', '王忠民'), ('吴双', '吴双')], max_length=32, verbose_name='寄回接收人')),
                ('back_date', models.DateField(blank=True, null=True, verbose_name='寄回日期')),
                ('charge', models.FloatField(blank=True, verbose_name='维修收费')),
                ('note', models.TextField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name': '设备寄出记录',
                'verbose_name_plural': '设备寄出记录',
                'ordering': ['-send_date'],
            },
        ),
        migrations.CreateModel(
            name='equip_maintain_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField(blank=True, max_length=128)),
                ('fault_startdate', models.DateTimeField(auto_now=True, null=True)),
                ('fault_enddate', models.DateTimeField(auto_now=True, null=True)),
                ('maintain_date', models.DateTimeField(auto_now=True, null=True)),
                ('staff', models.CharField(blank=True, max_length=32)),
                ('note', models.TextField(blank=True, default='', max_length=256)),
            ],
            options={
                'verbose_name': '设备维修记录',
                'verbose_name_plural': '设备维修记录',
            },
        ),
        migrations.CreateModel(
            name='equip_manu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('staff_name', models.CharField(blank=True, max_length=32)),
                ('address', models.CharField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
                ('mobile_phone', models.CharField(blank=True, max_length=128)),
                ('emai_address', models.EmailField(blank=True, max_length=128)),
                ('note', models.TextField(blank=True, default='', max_length=256)),
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
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('ip_mask', models.GenericIPAddressField(blank=True, default='255.255.255.0', null=True)),
                ('ip_gateway', models.GenericIPAddressField(blank=True, null=True)),
                ('sampling_rate', models.CharField(blank=True, choices=[('100sps', '每秒100点'), ('200sps', '每秒200点'), ('50sps', '每秒50点'), ('1spm', '每分1点'), ('1sph', '每小时1点')], max_length=32)),
                ('transmission_type', models.CharField(blank=True, choices=[('SDH', 'SDH'), ('3G', '3G'), ('Internet_VPN', 'Internet_VPN'), ('电台', '电台')], max_length=32)),
                ('install_date', models.DateField(blank=True, null=True)),
                ('remove_date', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name': '台站设备安装情况',
                'verbose_name_plural': '台站设备安装情况',
            },
        ),
        migrations.CreateModel(
            name='equip_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=32)),
                ('name', models.CharField(blank=True, max_length=32)),
                ('note', models.TextField(blank=True, default='', max_length=256)),
                ('manufacture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.equip_manu')),
            ],
            options={
                'verbose_name': '设备类型',
                'verbose_name_plural': '设备类型',
                'ordering': ['model'],
            },
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(blank=True, max_length=64)),
                ('note', models.TextField(blank=True, default='', max_length=256)),
                ('equip_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equip_type')),
            ],
            options={
                'verbose_name': '设备列表',
                'verbose_name_plural': '设备列表',
            },
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='station_img/')),
                ('note', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='measure_means',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('means', models.CharField(blank=True, default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_time', models.DateField(default=django.utils.timezone.now, verbose_name='计划发起时间')),
                ('to_do_time', models.DateField(blank=True, null=True, verbose_name='计划处理时间')),
                ('staff', models.CharField(blank=True, default='胡旭辉', max_length=32, verbose_name='人员')),
                ('plan', models.TextField(blank=True, max_length=256, verbose_name='计划内容')),
                ('status', models.CharField(blank=True, choices=[('1', '未完成'), ('2', '已完成'), ('3', '已放弃')], default='1', max_length=32, verbose_name='完成状态')),
            ],
            options={
                'verbose_name': '待办事件',
                'verbose_name_plural': '待办事件',
            },
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('name_en', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('name_cn', models.CharField(max_length=64)),
                ('project_source', models.CharField(blank=True, choices=[('十五', '十五'), ('十一五', '十一五'), ('十二五', '十二五'), ('背景场', '背景场'), ('十三五', '十三五'), ('九五', '九五')], default='十五', max_length=32)),
                ('longtitude', models.FloatField(blank=True, default=None, null=True)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('heigh', models.FloatField(blank=True, default=None, null=True)),
                ('lithology', models.CharField(blank=True, default='', max_length=32)),
                ('address', models.CharField(blank=True, default='', max_length=256)),
                ('staff_name', models.CharField(blank=True, default='', max_length=32)),
                ('phone', models.CharField(blank=True, default='', max_length=32)),
                ('note', models.TextField(blank=True, max_length=256)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.district')),
                ('measure_means', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.measure_means')),
            ],
            options={
                'verbose_name': '台站列表',
                'verbose_name_plural': '台站列表',
            },
        ),
        migrations.CreateModel(
            name='station_maintain_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(choices=[('济南', '济南'), ('泰安', '泰安'), ('潍坊', '潍坊'), ('德州', '德州'), ('滨州', '滨州'), ('莱芜', '莱芜'), ('青岛', '青岛'), ('烟台', '烟台'), ('日照', '日照'), ('东营', '东营'), ('济宁', '济宁'), ('菏泽', '菏泽'), ('聊城', '聊城'), ('临沂', '临沂'), ('枣庄', '枣庄'), ('淄博', '淄博'), ('威海', '威海'), ('省局', '省局')], default='烟台', max_length=32, verbose_name='地区')),
                ('intro', models.CharField(blank=True, max_length=64, verbose_name='故障描述')),
                ('report_date', models.DateTimeField(blank=True, null=True, verbose_name='报修时间')),
                ('reporter', models.CharField(blank=True, max_length=64, verbose_name='报修人或发现人')),
                ('fault_startdate', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('fault_enddate', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('staff', models.CharField(blank=True, max_length=32, verbose_name='处理人员')),
                ('maintain_process', models.TextField(blank=True, default='', max_length=256, verbose_name='处理经过')),
                ('note', models.TextField(blank=True, default='', max_length=256, verbose_name='备注')),
                ('equip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.equipment', verbose_name='设备')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.station', verbose_name='台站')),
            ],
            options={
                'verbose_name': '台站维修记录',
                'verbose_name_plural': '台站维修记录',
            },
        ),
        migrations.CreateModel(
            name='trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='开始时间')),
                ('end_date', models.DateField(verbose_name='结束时间')),
                ('place', models.CharField(max_length=32, verbose_name='出差地点')),
                ('purpose', models.CharField(max_length=256, verbose_name='出差目的')),
                ('staff', models.CharField(max_length=64, verbose_name='人员')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.station'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.station'),
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
        migrations.AddField(
            model_name='equip_maintain_record',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.station'),
        ),
        migrations.AddField(
            model_name='equip_delivery_record',
            name='back_equip_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='寄回设备类型', to='manager.equip_type', verbose_name='寄回设备类型'),
        ),
        migrations.AddField(
            model_name='equip_delivery_record',
            name='send_equip_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='寄出设备类型', to='manager.equip_type', verbose_name='寄出设备类型'),
        ),
    ]
