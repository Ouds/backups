# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django import template

register = template.Library()

#--------------------------------------
#           general
#--------------------------------------

import datetime

from ouds.utils.consts import JIE_QI
from ouds.city.updatecity import update_resources
from ouds.member.models import Union

@register.inclusion_tag('_base/general.ouds')
def general(user, city_id):

    # 节气
    today = datetime.date.today(); jie_qi = None
    for o in xrange(JIE_QI.__len__()):
        if JIE_QI[o][0] == today.month and JIE_QI[o][1] == today.day:
            jie_qi = JIE_QI[o][2]; break
    # 玩家资料
    profile = user.get_profile()
    # 当前城市
    city = update_resources(city_id, datetime.datetime.now())
    # 玩家城市列表
    city_list = profile.city_set.all()
    # 盟邦
    union = Union()
    if profile.union:
        union = Union.objects.get(id = profile.union)

    return {
            'jie_qi': jie_qi,
            'profile': profile,
            'union': union,
            'city_id': city_id,
            'city': city,
            'city_list': city_list,
           }

#--------------------------------------
#           city_info
#--------------------------------------

from ouds.city.models import City#, WareElement

@register.inclusion_tag('_base/city_info.ouds')
def city_info(city_id):

    city = City.objects.get(id = city_id)
    # 瓷器
    #ci_qi = city.ware_set.filter(ware_element = WareElement.objects.get(code__startswith = 'jiu_shui'))
    #print len(ci_qi)
    

    return {
            'city': city,
          
           }

