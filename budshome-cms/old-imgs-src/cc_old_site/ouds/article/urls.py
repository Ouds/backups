# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.conf.urls.defaults import patterns, url

modules = 'universe|asia|africa|north-america|south-america|antarctic|europe|oceanica|pacific-ocean|atlantic-ocean|indian-ocean|arctic-ocean|mall'

urlpatterns = patterns('ouds.article.views',
    url(r'^(' + modules + ')/$', 'module', name = 'module'),
    url(r'^(' + modules + ')/([^/]+)/$', 'catalog', name = 'catalog'),
    url(r'^(' + modules + ')/([^/]+)/([^/]+)/$', 'tag', name = 'tag'),
    url(r'^article/add_topic/$', 'add_topic', name='add_topic'),
    url(r'^(' + modules + ')/([^/]+)/(\d{4})/(\d{2})/(\d{2})/([^/]+)/$', 'topic', name = 'topic'),
    url(r'^article/([^/]+)/add_entry/$', 'add_entry', name='add_entry'),
    #url(r'^(' + modules + ')/([^/]+)/(\d{4})/(\d{2})/(\d{2})/([^/]+)/([^/]+)/$', 'entry', name = 'entry'),
    url(r'^article/search/$', 'search', name = 'search'),
#    url(r'^article/([^/]+)/comment/$', 'comment', name='comment'),
)

