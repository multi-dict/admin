# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='sex',
        ),
        migrations.AddField(
            model_name='word',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('neutral', 'Neutral')], max_length=10, null=True),
        ),
    ]