# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-01 03:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20181030_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 11, 1, 3, 20, 21, 267886, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
