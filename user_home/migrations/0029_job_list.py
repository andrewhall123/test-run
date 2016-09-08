# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 09:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0028_auto_20160903_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountant', models.IntegerField(default=0)),
                ('engineer', models.IntegerField(default=0)),
                ('designer', models.IntegerField(default=0)),
                ('software', models.IntegerField(default=0)),
                ('datas', django.contrib.postgres.fields.hstore.HStoreField(max_length=2000, null=True)),
                ('dummy_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_home.Dummy')),
            ],
        ),
    ]