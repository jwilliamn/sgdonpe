# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 01:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField(max_length=4000)),
                ('status', models.CharField(choices=[('V', 'Visado'), ('F', 'Firmado'), ('E', 'Enviado'), ('R', 'Redactado')], default='R', max_length=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-create_date',),
                'verbose_name_plural': 'Documentos',
                'verbose_name': 'Documento',
            },
        ),
        migrations.CreateModel(
            name='DocumentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
                'verbose_name_plural': 'Comentarios del documento',
                'verbose_name': 'Comentario del documento',
            },
        ),
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='docFiles/')),
                ('fileName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentoOficial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentFile')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='docOficialID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentoOficial'),
        ),
        migrations.AddField(
            model_name='document',
            name='firstAnexoID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Anexo'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anexo',
            name='idFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentFile'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='nextanexoID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Anexo'),
        ),
    ]
