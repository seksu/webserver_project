# Generated by Django 2.0.2 on 2018-03-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0011_auto_20180308_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='searching_detail',
            name='pos_body_h',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='pos_body_w',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='pos_body_x',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='pos_body_y',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='sd_b',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='sd_g',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='searching_detail',
            name='sd_r',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
