# Generated by Django 4.1.6 on 2023-03-11 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_trackerdata_data_trackerdata_compost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackerdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 18, 13, 13, 821831, tzinfo=datetime.timezone.utc)),
        ),
    ]
