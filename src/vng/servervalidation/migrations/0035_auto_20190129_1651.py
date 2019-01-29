# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-29 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0034_auto_20190129_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
        migrations.AlterField(
            model_name='expectedpostmanresult',
            name='expected_response',
            field=models.CharField(choices=[('200 OK', 'OK 200'), ('201 Created', 'CREATED 201'), ('301 Moved Permanently', 'MOVED 301'), ('302 Found', 'FOUND 302'), ('400 Bad Request', 'BAD REQUEST 400'), ('401 Unauthorized', 'UNAUTHORIZED 401'), ('403 Forbidden', 'FORBITTEN 403'), ('404 Not Found', 'NOT FOUND 404'), ('405 Method Not Allowed', 'METHOD NOT ALLOWED'), ('500 Internal Server Error', 'INTERNAL ERROR 500')], max_length=10),
        ),
        migrations.AlterField(
            model_name='postmantestresult',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
        migrations.AlterField(
            model_name='serverrun',
            name='status',
            field=models.CharField(choices=[('starting', 'starting'), ('running', 'running'), ('shutting down', 'shutting down'), ('stopped', 'stopped')], default='starting', max_length=20),
        ),
    ]
