# -*- coding: UTF-8 -*-

# Author: 张骛之
# Contact: ouds@thinkerunion.net
# File Name: comapny/templatetags.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 

from django import template

register = template.Library()

############

from django.contrib.sites.models import Site

@register.inclusion_tag('_base/link.ouds')
def link():
    '''网站友情链接'''
    
    sites = Site.objects.all()
    
    return {'sites': sites,}

############

from ouds.member.models import HelperCatalog

@register.inclusion_tag('_base/helper_catalog.ouds')
def helper_catalog():
    '''助手类别'''
    
    helper_catalogs = HelperCatalog.objects.all()
    
    return {'helper_catalogs': helper_catalogs,}

############

@register.inclusion_tag('_base/helper_entry.ouds')
def helper_entry(catalog_slug, language):
    '''助手条目'''

    helper_catalog = HelperCatalog.objects.get(slug = catalog_slug)
    helper_entries = helper_catalog.helperentry_set.filter(helper_catalog = helper_catalog, language = language, is_public = True)
    
    return {
            'language': language,
            'helper_catalog': helper_catalog,
            'helper_entries': helper_entries,
            }
