# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Searching_Detail
# Register your models here.

class SearchDetailAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp')

admin.site.register(Searching_Detail, SearchDetailAdmin)
