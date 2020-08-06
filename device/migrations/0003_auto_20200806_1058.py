# Generated by Django 2.2.12 on 2020-08-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_details_device_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_location',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_model',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='device',
            name='hostname',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='device',
            name='ios_version',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='device',
            name='vendor',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
