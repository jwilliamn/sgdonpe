# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('historiers', '0004_auto_20171104_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternStepHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlDestino', models.CharField(max_length=256)),
                ('codigoDocumentoExterno', models.IntegerField()),
                ('stepHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historiers.StepHistory')),
            ],
        ),
    ]
