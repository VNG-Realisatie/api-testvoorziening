# Generated by Django 2.2a1 on 2019-02-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0055_auto_20190206_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('starting', 'starting'), ('running', 'running'), ('shutting down', 'shutting down'), ('stopped', 'stopped')], default='starting', max_length=20),
        ),
    ]