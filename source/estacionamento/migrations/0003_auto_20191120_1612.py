# Generated by Django 2.2.1 on 2019-11-20 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0002_auto_20191120_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamento',
            name='entrada',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 20, 16, 12, 48, 205789)),
        ),
    ]
