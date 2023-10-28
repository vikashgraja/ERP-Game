# Generated by Django 4.2.5 on 2023-10-13 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_score_end_time_alter_score_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='time_taken',
            field=models.TimeField(default=datetime.datetime.now, null=True),
        ),
    ]
