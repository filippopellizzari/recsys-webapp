# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-24 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0025_survey_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionorder',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_to_survey', to='surveys.Question'),
        ),
        migrations.AlterField(
            model_name='questionorder',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_to_question', to='surveys.Survey'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(through='surveys.QuestionOrder', to='surveys.Question'),
        ),
    ]