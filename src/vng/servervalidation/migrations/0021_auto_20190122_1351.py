# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0020_auto_20190121_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverrun',
            name='log',
        ),
        migrations.RemoveField(
            model_name='testscenario',
            name='validation_file',
        ),
        migrations.AddField(
            model_name='testscenariourl',
            name='log',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='/files/log'),
        ),
        migrations.AddField(
            model_name='testscenariourl',
            name='validation_file',
            field=models.FileField(default=None, null=True, upload_to='', verbose_name='/files/uploaded_files'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]
