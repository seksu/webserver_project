# Generated by Django 2.0.2 on 2018-03-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0012_auto_20180315_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searching_detail',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
