# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0031_auto_20160903_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='all',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
