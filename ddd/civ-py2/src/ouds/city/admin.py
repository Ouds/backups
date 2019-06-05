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

from ouds.city.models import City, BuildingElement, Building, ImprovingBuilding, ProfessionalElement, Professional, ImprovingProfessional, \
WareElement, Ware, ProducingWare, ForceElement, Force, TrainingForce

class CityAdmin(admin.ModelAdmin):
    search_fields = ('profile__user__username', 'name',)

# admin.site.register(City, CityAdmin)

class BuildingElementAdmin(admin.ModelAdmin):
    search_fields = ('name', 'time', 'civilization_value',)
    filter_horizontal = ('tech_element',)

admin.site.register(BuildingElement, BuildingElementAdmin)

class BuildingAdmin(admin.ModelAdmin):
    search_fields = ('city__name', 'building_element__name', 'location',)

admin.site.register(Building, BuildingAdmin)

class ImprovingBuildingAdmin(admin.ModelAdmin):
    search_fields = ('city__name', 'building__building_element__name',)

admin.site.register(ImprovingBuilding, ImprovingBuildingAdmin)

class ProfessionalElementAdmin(admin.ModelAdmin):
    search_fields = ('name', 'building_element__name')
    list_filter = ('building_element',)

admin.site.register(ProfessionalElement, ProfessionalElementAdmin)

class ProfessionalAdmin(admin.ModelAdmin):
    search_fields = ('name', 'building__building_element__name', 'professional_element__name')
    list_filter = ('professional_element',)

admin.site.register(Professional, ProfessionalAdmin)

class ImprovingProfessionalAdmin(admin.ModelAdmin):
    search_fields = ('professional__professional_element__name',)

admin.site.register(ImprovingProfessional, ImprovingProfessionalAdmin)

class WareElementAdmin(admin.ModelAdmin):
    search_fields = ('name', 'building_element__name')
    list_filter = ('building_element',)

admin.site.register(WareElement, WareElementAdmin)

class WareAdmin(admin.ModelAdmin):
    search_fields = ('name', 'ware_element__name')
    list_filter = ('ware_element',)

admin.site.register(Ware, WareAdmin)

class ProducingWareAdmin(admin.ModelAdmin):
    search_fields = ('ware__ware_element__name',)

admin.site.register(ProducingWare, ProducingWareAdmin)

class ForceElementAdmin(admin.ModelAdmin):
    search_fields = ('name', 'building_element__name')
    list_filter = ('building_element',)
    filter_horizontal = ('restraint',)

admin.site.register(ForceElement, ForceElementAdmin)

class ForceAdmin(admin.ModelAdmin):
    search_fields = ('name', 'force_element__name')
    list_filter = ('force_element',)

admin.site.register(Force, ForceAdmin)

class TrainingForceAdmin(admin.ModelAdmin):
    search_fields = ('force__force_element__name',)

admin.site.register(TrainingForce, TrainingForceAdmin)


