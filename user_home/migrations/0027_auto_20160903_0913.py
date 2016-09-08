# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 09:13
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0026_auto_20160903_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_list',
            name='data',
        ),
        migrations.AddField(
            model_name='job_list',
            name='datas',
            field=django.contrib.postgres.fields.hstore.HStoreField(max_length=2000, null=True),
        ),
    ]
