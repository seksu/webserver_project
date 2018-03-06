# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Camera_Detail, Company
from django.contrib import admin

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class CameraDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'token', 'date', 'get_company')

    def get_company(self, camera):
        return camera.company.name
    get_company.short_description = 'Company'

admin.site.register(Camera_Detail, CameraDetailAdmin)
admin.site.register(Company, CompanyAdmin)
