# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0010_auto_20171211_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imagelink',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]