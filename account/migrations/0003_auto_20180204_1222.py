# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
        ('account', '0002_auto_20180126_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camera.Company'),
        ),
        migrations.AddField(
            model_name='account',
            name='facepath',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
