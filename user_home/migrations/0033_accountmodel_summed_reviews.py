# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0032_accountmodel_all'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='summed_reviews',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]