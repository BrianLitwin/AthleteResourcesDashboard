# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-21 03:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_exercises_onerepmax'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_metrics',
            old_name='personalRecords',
            new_name='personalRecord',
        ),
    ]
