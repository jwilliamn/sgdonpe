# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stephistory',
            name='when',
        ),
        migrations.AddField(
            model_name='stephistory',
            name='whenTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
