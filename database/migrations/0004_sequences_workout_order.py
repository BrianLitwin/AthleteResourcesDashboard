# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-13 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_sequences'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequences',
            name='workout_order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
