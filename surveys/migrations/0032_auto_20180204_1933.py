# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-04 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0031_response_completed_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionorder',
            options={'ordering': ('the_order',)},
        ),
        migrations.AddField(
            model_name='questionorder',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]