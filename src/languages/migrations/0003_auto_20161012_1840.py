# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20161012_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languages',
            options={'verbose_name': 'Language', 'verbose_name_plural': 'Languages'},
        ),
    ]