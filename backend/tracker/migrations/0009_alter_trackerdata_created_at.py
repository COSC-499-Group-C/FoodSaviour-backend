# Generated by Django 4.1.7 on 2023-03-29 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_alter_trackerdata_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackerdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 29, 23, 12, 25, 463022, tzinfo=datetime.timezone.utc)),
        ),
    ]
