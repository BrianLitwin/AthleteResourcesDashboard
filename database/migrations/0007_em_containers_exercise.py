# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-14 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_exercises'),
    ]

    operations = [
        migrations.AddField(
            model_name='em_containers',
            name='exercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='database.Exercises'),
            preserve_default=False,
        ),
    ]
