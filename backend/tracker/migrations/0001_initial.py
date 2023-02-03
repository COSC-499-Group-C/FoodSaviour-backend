# Generated by Django 4.1.5 on 2023-02-03 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Waste Types',
            },
        ),
        migrations.CreateModel(
            name='TrackerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('data', models.JSONField(default={'data': {'data-point-1': 'example 1', 'data-point-2': 'example 2'}}, verbose_name='Tracker Data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('waste_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.wastetype')),
            ],
            options={
                'verbose_name_plural': 'Tracker Data',
            },
        ),
    ]
