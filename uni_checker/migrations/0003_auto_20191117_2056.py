# Generated by Django 2.2.7 on 2019-11-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_checker', '0002_auto_20191116_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='deadline',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='is_completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
