# Generated by Django 2.1.4 on 2018-12-22 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_auto_20181222_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2018, 12, 22)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 12, 22, 15, 36, 24, 543856, tzinfo=utc)),
        ),
    ]
