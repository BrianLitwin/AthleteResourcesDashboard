# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-14 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_em_containers_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_Metrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_string', models.CharField(max_length=50)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_metrics', to='database.EM_Containers')),
            ],
        ),
    ]
