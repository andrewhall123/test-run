# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0014_job_list_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='user_review',
            field=models.FloatField(default=0.0),
        ),
    ]
