# Generated by Django 2.0 on 2018-02-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20180225_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station_maintain_record',
            name='reporter',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='报修人或发现人'),
        ),
    ]