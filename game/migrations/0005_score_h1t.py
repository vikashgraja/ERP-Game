# Generated by Django 4.2.6 on 2023-10-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_score_end_time_alter_score_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='H1t',
            field=models.IntegerField(default=2),
        ),
    ]
