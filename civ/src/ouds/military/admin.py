# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/city/admin.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: admin file of city module.
#===============================================================================

from django.contrib import admin

from ouds.military.models import Force, General

class ForceAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Force, ForceAdmin)

class GeneralAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(General, GeneralAdmin)
