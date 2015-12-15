# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 10:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0026_auto_20151212_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.Type'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 10, 58, 36, 878701, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 10, 58, 36, 878743, tzinfo=utc)),
        ),
    ]