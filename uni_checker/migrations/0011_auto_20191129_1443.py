# Generated by Django 2.2.7 on 2019-11-29 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uni_checker', '0010_auto_20191123_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='row',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='item',
            name='has_deadline',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 11, 29, 14, 43, 8, 552351, tzinfo=utc)),
        ),
    ]
