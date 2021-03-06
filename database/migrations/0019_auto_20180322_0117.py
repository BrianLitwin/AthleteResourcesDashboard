# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-22 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_metric_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric_info',
            name='metric',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metric_info',
            name='output_label',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metric_info',
            name='sort_in_ascending_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='metric_info',
            name='unit_of_measurement',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
