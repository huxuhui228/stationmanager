# Generated by Django 2.0 on 2018-02-08 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0033_remove_station_measure_means'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='measure_means',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.measure_means'),
        ),
    ]
