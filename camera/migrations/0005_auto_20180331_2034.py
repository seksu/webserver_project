# Generated by Django 2.0.2 on 2018-03-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0004_auto_20180331_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera_detail',
            name='latitude_t',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='camera_detail',
            name='longitude_t',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='camera_detail',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='camera_detail',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
