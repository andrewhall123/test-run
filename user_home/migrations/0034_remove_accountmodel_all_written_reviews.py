# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0033_accountmodel_summed_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='all_written_reviews',
        ),
    ]