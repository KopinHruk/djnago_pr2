# Generated by Django 2.2.7 on 2019-11-18 16:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uni_checker', '0006_auto_20191118_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 16, 27, 48, 344531, tzinfo=utc)),
        ),
    ]
