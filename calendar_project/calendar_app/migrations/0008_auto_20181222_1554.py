# Generated by Django 2.1.4 on 2018-12-22 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0007_auto_20181222_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default='12:00'),
        ),
    ]