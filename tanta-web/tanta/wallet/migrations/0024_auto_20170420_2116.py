# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 21:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0023_auto_20170420_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
