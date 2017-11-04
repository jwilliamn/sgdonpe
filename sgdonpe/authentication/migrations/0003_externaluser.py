# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_internaluser_coddependencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('codigoUsuario', models.CharField(max_length=8)),
                ('codDependencia', models.CharField(default='ING', max_length=8)),
                ('dependencia', models.CharField(max_length=256)),
                ('urlUser', models.CharField(max_length=128)),
                ('dni', models.CharField(max_length=12)),
            ],
        ),
    ]