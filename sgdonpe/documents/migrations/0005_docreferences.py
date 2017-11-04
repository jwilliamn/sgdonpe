# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_documentviewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocReferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docParentReferencing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document')),
            ],
        ),
    ]
