# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_auto_20161128_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='name',
            new_name='text',
        ),
    ]
