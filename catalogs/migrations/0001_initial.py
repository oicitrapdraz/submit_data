# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-02 23:00
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('creation_date', models.DateField(verbose_name='creation date')),
                ('creators', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=35), size=10)),
                ('subjects', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=35), size=5)),
                ('instrument', models.CharField(max_length=50)),
                ('facility', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('AR', 'Archive'), ('BI', 'Bibliography'), ('CA', 'Catalog'), ('JO', 'Journal')], default='CA', max_length=2)),
                ('coverage_profile', models.CharField(max_length=200)),
                ('coverage_waveband', models.CharField(choices=[('OR', 'One of Radio'), ('OP', 'Optical'), ('UV', 'UV')], default='OR', max_length=2)),
            ],
        ),
    ]