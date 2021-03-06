# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_home', '0016_auto_20160902_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
