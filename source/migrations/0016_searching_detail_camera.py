# Generated by Django 2.0.2 on 2018-03-21 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_camera_detail_floor'),
        ('source', '0015_auto_20180320_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='searching_detail',
            name='camera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camera.Camera_Detail'),
        ),
    ]
