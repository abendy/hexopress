# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexo', '0005_blogsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsettings',
            name='ga_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
