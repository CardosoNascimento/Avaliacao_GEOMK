# Generated by Django 2.2.1 on 2019-11-27 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='entrada',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 16, 42, 6, 155254)),
        ),
    ]
