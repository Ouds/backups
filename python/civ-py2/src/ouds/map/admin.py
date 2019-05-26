# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/map/admin.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: admin file of map module.
#===============================================================================

from django.contrib import admin

from ouds.map.models import Coordinate

class CoordinateAdmin(admin.ModelAdmin):
    search_fields = ('longitude', 'latitude', 'property')

# admin.site.register(Coordinate, CoordinateAdmin)

