# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20160903_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionaire_review_model',
            name='written',
        ),
    ]
