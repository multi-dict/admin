# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionaries',
            options={'verbose_name': 'Dictionary', 'verbose_name_plural': 'Dictionaries'},
        ),
    ]