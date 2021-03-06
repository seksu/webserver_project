# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('source', '0002_auto_20180126_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searching_detail',
            old_name='PositionH',
            new_name='position_h',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='PositionW',
            new_name='position_w',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='PositionX',
            new_name='position_x',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='PositionY',
            new_name='position_y',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='ShirtColorB',
            new_name='shirtcolor_b',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='ShirtColorG',
            new_name='shirtcolor_g',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='ShirtColorR',
            new_name='shirtcolor_r',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='TimeLapse',
            new_name='timelapse',
        ),
        migrations.RenameField(
            model_name='searching_detail',
            old_name='TimeStamp',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='searching_detail',
            name='FacePath',
        ),
        migrations.RemoveField(
            model_name='searching_detail',
            name='Token',
        ),
        migrations.RemoveField(
            model_name='searching_detail',
            name='VideoPath',
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='facepath',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='videopath',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
