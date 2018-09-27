# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-25 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_currency_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='id',
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='code'),
        ),
    ]
