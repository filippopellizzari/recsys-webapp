# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-04 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0033_auto_20180204_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='the_order',
        ),
    ]