# Generated by Django 2.0 on 2018-04-18 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='station',
            options={'ordering': ['district', 'name_cn'], 'verbose_name': '台站列表', 'verbose_name_plural': '台站列表'},
        ),
    ]
