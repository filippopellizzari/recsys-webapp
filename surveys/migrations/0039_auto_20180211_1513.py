# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-11 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0038_auto_20180211_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='survey_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey'),
        ),
    ]
