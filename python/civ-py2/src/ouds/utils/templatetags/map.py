# -*- coding: UTF-8 -*-

# Author: 张骛之
# Contact: ouds@thinkerunion.net
# File Name: comapny/templatetags.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 

from django import template

from ouds.city.models import City

register = template.Library()

#===============================================================================
# 根据坐标主键取得在其处城市
#===============================================================================

@register.filter
def is_occupied(coordinate_id):
    '''根据坐标主键取得在其处城市'''
    
    city = City()
    try:
        city = City.objects.get(coordinate = coordinate_id)
    except city.DoesNotExist:
        return 0

    return city
