# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20170819_1552'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='BitcoinHistory',
        ),
        migrations.RenameModel(
            old_name='LiveData',
            new_name='BitcoinLiveData',
        ),
    ]
