# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-29 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_feautured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='feautured',
            new_name='featured',
        ),
    ]
