# Generated by Django 2.0 on 2018-04-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20180418_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip_maintain_record',
            name='staff',
            field=models.CharField(blank=True, choices=[('胡旭辉', '胡旭辉'), ('李小晗', '李小晗'), ('王杰民', '王杰民'), ('曲利', '曲利'), ('冯志军', '冯志军'), ('马丕峰', '马丕峰'), ('吴双', '吴双')], max_length=32),
        ),
    ]
