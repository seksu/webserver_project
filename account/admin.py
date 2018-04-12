# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):

	list_display = ('id', 'email', 'get_company')

	def get_company(self, account):
		return account.company.name if account.company else "-"
	get_company.short_description = "Company"

admin.site.register(Account, AccountAdmin)
