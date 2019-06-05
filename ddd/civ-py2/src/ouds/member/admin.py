# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/member/admin.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: admin file of member module.
#===============================================================================

from django.contrib import admin

from ouds.member.models import Profile, Message, Union, TechElement, Tech, ImprovingTech, HelperCatalog, HelperEntry, Bug

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

admin.site.register(Profile, ProfileAdmin)

class UnionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'website',)

admin.site.register(Union, UnionAdmin)

class MessageAdmin(admin.ModelAdmin):
    search_fields = ('profile__user__username', 'title', 'receiver')

admin.site.register(Message, MessageAdmin)

class TechElementAdmin(admin.ModelAdmin):
    search_fields = ('name', 'prestige',)
    filter_horizontal = ('tech_element',)

admin.site.register(TechElement, TechElementAdmin)

class TechAdmin(admin.ModelAdmin):
    search_fields = ('profile__user__name', 'tech_element__name',)

admin.site.register(Tech, TechAdmin)

class ImprovingTechAdmin(admin.ModelAdmin):
    search_fields = ('profile__user__name', 'tech__tech_element__name',)

admin.site.register(ImprovingTech, ImprovingTechAdmin)

class HelperCatalogAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(HelperCatalog, HelperCatalogAdmin)

class HelperEntryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug', 'helper_catalog__name', 'content')
    prepopulated_fields = {'slug': ('name', 'language')}
    list_filter = ('language', 'helper_catalog', 'is_public')

admin.site.register(HelperEntry, HelperEntryAdmin)

class BugAdmin(admin.ModelAdmin):
    search_fields = ('title', 'level', 'submitor', 'submit_time', 'is_corrected', 'reeditor')
    list_display = ('title', 'level', 'submitor', 'submit_time', 'is_corrected', 'reeditor')
    list_filter = ('is_corrected', 'level', 'submit_time', 'submitor', 'reeditor')
    date_hierarchy = 'submit_time'

admin.site.register(Bug, BugAdmin)
