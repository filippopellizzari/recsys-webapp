# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-07 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Recommender',
        ),
    ]
