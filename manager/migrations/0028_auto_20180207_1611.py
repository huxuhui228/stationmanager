# Generated by Django 2.0 on 2018-02-07 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0027_district_measure_means'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.district'),
        ),
    ]
