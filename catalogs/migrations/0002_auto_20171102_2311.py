# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-02 23:11
from __future__ import unicode_literals

from django.db import models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField('catalog', 'creation_date', models.DateTimeField('creation date'))
    ]
