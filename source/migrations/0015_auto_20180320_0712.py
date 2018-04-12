# Generated by Django 2.0.2 on 2018-03-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0014_remove_searching_detail_recognition_face'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searching_detail',
            name='pos_body_h',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='pos_body_w',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='pos_body_x',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='pos_body_y',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='position_h',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='position_w',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='position_x',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='position_y',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='sd_b',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='sd_g',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='sd_r',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='shirtcolor_b',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='shirtcolor_g',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='shirtcolor_r',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='searching_detail',
            name='timelapse',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]