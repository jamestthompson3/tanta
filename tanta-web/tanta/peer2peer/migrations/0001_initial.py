# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 05:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender', models.CharField(max_length=200)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('amount_remaining', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('next_payment_due', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_payment_made', models.DateTimeField(default=django.utils.timezone.now)),
                ('loan_length', models.IntegerField()),
                ('time_remaining', models.DateTimeField(default=django.utils.timezone.now)),
                ('initial_amount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]