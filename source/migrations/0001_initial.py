# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Searching_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Token', models.CharField(max_length=30, null=True)),
                ('TimeStamp', models.DateTimeField()),
                ('FacePath', models.CharField(max_length=30, null=True)),
                ('TimeLapse', models.PositiveIntegerField(default=0)),
                ('VideoPath', models.CharField(max_length=30, null=True)),
                ('PositionX', models.PositiveIntegerField(default=0)),
                ('PositionY', models.PositiveIntegerField(default=0)),
                ('PositionW', models.PositiveIntegerField(default=0)),
                ('PositionH', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
