# Generated by Django 2.0.2 on 2018-03-19 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0013_auto_20180319_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searching_detail',
            name='recognition_face',
        ),
    ]
