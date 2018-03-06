# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from account.models import Account
from django.db import models

# Create your models here.

class Searching_Detail(models.Model):
	timestamp = models.DateTimeField()
	face_path = models.CharField(max_length=200, null=True)
	fullbody_path = models.CharField(max_length=200, null=True)
	videopath = models.CharField(max_length=200, null=True)
	timelapse = models.PositiveIntegerField(default=0)
	position_x = models.PositiveIntegerField(default=0)
	position_y = models.PositiveIntegerField(default=0)
	position_w = models.PositiveIntegerField(default=0)
	position_h = models.PositiveIntegerField(default=0)
	shirtcolor_r = models.PositiveIntegerField(default=0)
	shirtcolor_g = models.PositiveIntegerField(default=0)
	shirtcolor_b = models.PositiveIntegerField(default=0)
	account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
