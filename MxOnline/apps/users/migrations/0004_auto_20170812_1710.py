# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-12 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170811_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecode',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='\u90ae\u7bb1'),
        ),
    ]
