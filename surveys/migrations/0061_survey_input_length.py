# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-11 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0060_auto_20180607_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='input_length',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
