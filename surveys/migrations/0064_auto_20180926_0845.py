# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-26 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0063_auto_20180918_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='algorithms',
            field=models.CharField(max_length=500, null=True),
        ),
    ]