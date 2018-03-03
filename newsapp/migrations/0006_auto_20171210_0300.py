# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_auto_20171209_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.AddField(
            model_name='comment',
            name='tickleFK',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_UserFK', to='newsapp.Users'),
        ),
    ]