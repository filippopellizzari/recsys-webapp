# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0051_auto_20180325_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={},
        ),
        migrations.AlterModelOptions(
            name='optionorder',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AddField(
            model_name='optionorder',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
