# Generated by Django 2.1.4 on 2018-12-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kickstarter',
            name='converted_pledged_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]