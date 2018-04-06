# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-13 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20180313_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coreDataID', models.IntegerField()),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Workouts')),
            ],
        ),
    ]