# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-16 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_exercise_metrics_set_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise_metrics',
            name='coreDataID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]