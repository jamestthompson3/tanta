# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0031_auto_20170427_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='userid',
            field=models.IntegerField(null=True),
        ),
    ]