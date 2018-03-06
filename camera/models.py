# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Camera_Detail(models.Model):
    token = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    date = models.DateTimeField()
    name = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
