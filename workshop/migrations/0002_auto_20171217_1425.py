# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 05:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='do_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 17, 5, 25, 27, 240233, tzinfo=utc)),
        ),
    ]
