# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='school',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='board.School'),
            preserve_default=False,
        ),
    ]