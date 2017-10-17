# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0036_auto_20170429_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.CharField(choices=[('borrow', 'borrow'), ('lend', 'lend')], default='lend', max_length=6),
        ),
    ]
