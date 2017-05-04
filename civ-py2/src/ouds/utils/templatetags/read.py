# -*- coding: UTF-8 -*-

# Author: 张骛之
# Contact: ouds@thinkerunion.net
# File Name: comapny/templatetags.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 

import datetime

from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()

###############################

@register.filter
def dict_filter(dict, key):
    '''取得字典中键对应的值'''

    return dict[key]

###############################

@register.filter
def make_tuple(key, value):
    '''组合一个元组'''

    if type(key) is tuple:
        key += (value,)
    else:
        key = (key, value)

    return key

##############################

@register.filter
def tuple_filter(key, tuple_name):
    '''根据键搜索元组中子元组的值'''

    exec 'from ouds.utils.consts import %s as tuple_name' %tuple_name
    for o in xrange(tuple_name.__len__()):
        if tuple_name[o][0] == key:
            return _(tuple_name[o][1])

##############################

@register.filter
def int2time(seconds, multiple = 1):
    '''转化秒数为时间'''

    time = datetime.timedelta(seconds = seconds * multiple)
    
    return {
            'days': time.days,
            'time': datetime.timedelta(seconds = time.seconds),
           }

##################################

@register.filter
def time2int(time):
    '''转化时间为天、秒数'''
    
    time -= datetime.datetime.now()
    days = time.days; seconds = time.seconds
    if time.days < 0:
        days = 0; seconds = 0
    
    return {
            'days': days,
            'time': seconds,
           }

#################################

from ouds.utils.consts import INCREMENT

@register.filter
def level_arithmetic(level, meta = 108):
    '''根据级别算出相应的耗量、增量'''

    f = 0
    for m in xrange(1, level/INCREMENT+1):
        f += m

    return (f * INCREMENT + level%INCREMENT * (level/INCREMENT + 1)) * meta

##################################

@register.filter
def subtract(subtracter, subtracted):
    '''减'''
    
    return subtracted - subtracter

##################################

@register.filter
def multiply(multiplied, multiplier = 0.01):
    '''乘'''
    
    return int(multiplied * multiplier)

############################

@register.filter
def element_level(level):
    '''根据专家将要升级的级别判断其需物资级别'''

    if level == 0:
        pass
    elif level <= INCREMENT:
        level = 1
    elif INCREMENT + 1 <= level <= INCREMENT * 2:
        level = 2
    elif INCREMENT * 2 + 1 <= level <= INCREMENT * 3:
        level = 3
    elif INCREMENT * 3 + 1 <= level <= INCREMENT * 4:
        level = 4
    else:
        level = 5
    
    return level

##################################

from ouds.member.models import Tech

@register.filter
def pre_techs(is_exist_tech, profile):
    '''科技前提'''

    is_exist = is_exist_tech[0]
    pre_techs = []
    if is_exist:
        tech = is_exist_tech[1]
        for pre_tech_element in tech.tech_element.tech_element.all():
            pre_tech = Tech.objects.filter(profile = profile, tech_element = pre_tech_element)
            if pre_tech:
                if pre_tech[0].level < tech.level + tech.improvingtech_set.count() + 1:
                    pre_techs.append(pre_tech[0])
            else:
                tech_without = Tech()
                tech_without.profile = profile
                tech_without.tech_element = pre_tech_element
                tech_without.level = 0
                tech_without.end_time = datetime.datetime.now()
                pre_techs.append(tech_without)
    else:
        tech_element = is_exist_tech[1]
        for pre_tech_element in tech_element.tech_element.all():
            pre_tech = Tech.objects.filter(profile = profile, tech_element = pre_tech_element)
            if not pre_tech:
                tech_without = Tech()
                tech_without.profile = profile
                tech_without.tech_element = pre_tech_element
                tech_without.level = 0
                tech_without.end_time = datetime.datetime.now()
                pre_techs.append(tech_without)
    
    return pre_techs

##################################

@register.filter
def need_techs(is_exist_building, profile):
    '''建筑科技前提'''

    is_exist = is_exist_building[0]
    need_techs = []
    if is_exist:
        building = is_exist_building[1]
        building_tech_element = building.building_element.tech_element.filter(prestige__lte = element_level(building.level + building.improvingbuilding_set.count() + 1))

        for tech_element in building_tech_element:
            tech = Tech.objects.filter(profile = profile, tech_element = tech_element)
            if tech:
                if tech[0].level <= element_level(building.level + building.improvingbuilding_set.count() + 1) - tech[0].tech_element.prestige:
                    need_techs.append(tech[0])
            else:
                tech_without = Tech()
                tech_without.profile = profile
                tech_without.tech_element = tech_element
                tech_without.level = 0
                tech_without.end_time = datetime.datetime.now()
                need_techs.append(tech_without)
    else:
        building_element = is_exist_building[1]
        building_tech_element = building_element.tech_element.filter(prestige = 1)

        for tech_element in building_tech_element:
            tech = Tech.objects.filter(profile = profile, tech_element = tech_element)
            if not tech:
                tech_without = Tech()
                tech_without.profile = profile
                tech_without.tech_element = tech_element
                tech_without.level = 0
                tech_without.end_time = datetime.datetime.now()
                need_techs.append(tech_without)
    
    return need_techs

##################################

@register.filter
def ware_element_id(level, code):
    '''判断物资元素ID'''

    if code == 'mu-qi':
        ware_element_id = level
    elif code == 'ci-qi':
        ware_element_id = 6 + level - 1
    elif code == 'jiu-shui':
        ware_element_id = 11 + level - 1
    elif code == 'yu-qi':
        ware_element_id = 16 + level - 1
        
    return ware_element_id

##################################

from ouds.city.models import WareElement

@register.filter
def city_ware(level_code, city):
    '''城市拥有某类物资的数量'''

    try:
        return city.ware_set.get(ware_element = WareElement(id = ware_element_id(level_code[0], level_code[1])))
    except:
        from ouds.city.models import Ware
        return Ware(ware_element = WareElement.objects.get(id = ware_element_id(level_code[0], level_code[1])), amount = 0)

##################################

@register.filter
def professional_increment(level):
    '''判断物资元素ID'''

    return level - (element_level(level) * 9 - 9)

##################################

from ouds.city.models import ForceElement

@register.filter
def city_force(force_element_id, city):
    '''城市拥有某类武力的数量'''

    try:
        return city.force_set.get(force_element = ForceElement(id = force_element_id))
    except:
        from ouds.city.models import Force
        return Force(amount = 0)

##################################

@register.filter
def is_educable(professional_amount, building):
    '''可否训练新的专家'''

    id = building.building_element.id
    is_capital = building.city.is_capital
    is_educable = False
    if id not in (34, 35, 36, 37, 38, 39) and building.level > 0:
        # 兵部，武馆，魔法学校
        if id in (3, 14, 15):
            if is_capital:
                if professional_amount < 4:
                    is_educable = True
            else:
                if professional_amount < 3:
                    is_educable = True
        # 船坞
        elif id == 4:
            if is_capital:
                if professional_amount < 3:
                    is_educable = True
            else:
                if professional_amount < 2:
                    is_educable = True
        # 鸿胪寺
        elif id == 20:
            if professional_amount < 1:
                is_educable = True
        # 其它有专家的建筑
        else:
            if is_capital:
                if professional_amount < 2:
                    is_educable = True
            else:
                if professional_amount < 1:
                    is_educable = True

    return is_educable

##################################

#@register.filter
#def is_training(building_element_id):
#    ''''''


