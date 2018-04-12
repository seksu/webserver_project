# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from account.models import Account
from camera.models import Camera_Detail
from django.db import models

# Create your models here.

class Searching_Detail(models.Model):
	timestamp = models.DateTimeField(null=True)
	face_path = models.CharField(max_length=200, null=True)
	fullbody_path = models.CharField(max_length=200, null=True)
	video_path = models.CharField(max_length=200, null=True)
	timelapse = models.PositiveIntegerField(default=0, null=True)
	position_x = models.PositiveIntegerField(default=0, null=True)
	position_y = models.PositiveIntegerField(default=0, null=True)
	position_w = models.PositiveIntegerField(default=0, null=True)
	position_h = models.PositiveIntegerField(default=0, null=True)
	shirtcolor_r = models.PositiveIntegerField(default=0, null=True)
	shirtcolor_g = models.PositiveIntegerField(default=0, null=True)
	shirtcolor_b = models.PositiveIntegerField(default=0, null=True)
	pos_body_x = models.PositiveIntegerField(default=0, null=True)
	pos_body_y = models.PositiveIntegerField(default=0, null=True)
	pos_body_w = models.PositiveIntegerField(default=0, null=True)
	pos_body_h = models.PositiveIntegerField(default=0, null=True)
	sd_r = models.PositiveIntegerField(default=0, null=True)
	sd_g = models.PositiveIntegerField(default=0, null=True)
	sd_b = models.PositiveIntegerField(default=0, null=True)
	account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
	camera = models.ForeignKey(Camera_Detail, null=True, on_delete=models.CASCADE)
