
# Generated by Django 4.1.7 on 2023-03-29 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_trackerdata_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackerdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 29, 22, 38, 50, 10568, tzinfo=datetime.timezone.utc)),
        ),
    ]
