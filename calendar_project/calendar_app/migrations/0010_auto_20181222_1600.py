# Generated by Django 2.1.4 on 2018-12-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0009_auto_20181222_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
    ]