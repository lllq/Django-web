# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-11 14:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecode',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4'),
        ),
    ]
