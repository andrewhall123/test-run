# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 10:20
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0012_job_list'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name='job_list',
            name='software',
            field=models.IntegerField(default=0),
        ),
    ]
