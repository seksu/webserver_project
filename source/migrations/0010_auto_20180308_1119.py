# Generated by Django 2.0.2 on 2018-03-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0009_auto_20180307_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searching_detail',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
