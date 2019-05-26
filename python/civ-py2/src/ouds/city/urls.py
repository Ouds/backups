# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/member/urls.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: urls file of member module.
#===============================================================================

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ouds.city.views',
        (r'^$', 'city'),
        
        (r'^location/$', 'location'),
        (r'^location/build/$', 'location_build'),
        (r'^building/([0-9a-f]{32})/$', 'building'),
        (r'^building/improve/$', 'building_improve'),
        
        (r'^professional/educate/$', 'professional_educate'),
        (r'^professional/improve/$', 'professional_improve'),
       )
