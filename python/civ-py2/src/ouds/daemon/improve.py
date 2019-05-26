#! /home/oudsus/bin/python
# -*-coding:UTF-8-*-#

# Author: 张骛之
# Contact: ouds@thinkerunion.net
# File Name: daemon.py
# Revision: 0.1
# Date: 2009-4-16 19:15
# Description: 

import sys
#sys.path.append('/home/oudsus/ThinkerUnion/Civilization')

import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'ouds.settings'

import time
import datetime

from ouds.utils.templatetags.read import level_arithmetic

# 科技升级
from ouds.member.models import Profile, Tech, ImprovingTech

# 建筑升级
from ouds.city.models import City, Building, ImprovingBuilding
from ouds.city.updatecity import update_resources

# 专家升级
from ouds.city.models import Professional, ImprovingProfessional

sleep = 0

while True:

    # 科技升级
    now = datetime.datetime.now(); profile = Profile(); tech = Tech()
    improving_tech_list = ImprovingTech.objects.filter(end_time__lt = now)
    for improving_tech in improving_tech_list:
        tech = improving_tech.tech
        tech.level = improving_tech.level
        tech.save()

        profile = tech.profile
        profile.prestige += tech.tech_element.prestige
        profile.save()

        improving_tech.delete()
        sleep += 1
        if sleep%100 == 0: time.sleep(1)

    del now, tech, profile
    time.sleep(1)
    

    # 建筑升级
    now = datetime.datetime.now(); city = City(); building = Building()
    improving_building_list = ImprovingBuilding.objects.filter(end_time__lt = now)
    for improving_building in improving_building_list:
        # 建筑升级/建造完成
        building = improving_building.building
        building.level = improving_building.level
        building.save()
        # 改变城市数值
        city = update_resources(building.city.id, now)
        city.food_speed += level_arithmetic(building.level, building.building_element.food_speed)
        city.food_storage += level_arithmetic(building.level, building.building_element.food_storage)
        city.wood_speed += level_arithmetic(building.level, building.building_element.wood_speed)
        city.wood_storage += level_arithmetic(building.level, building.building_element.wood_storage)
        city.ore_speed += level_arithmetic(building.level, building.building_element.ore_speed)
        city.ore_storage += level_arithmetic(building.level, building.building_element.ore_storage)
        city.gold_storage += level_arithmetic(building.level, building.building_element.gold_storage)
        city.people_storage += level_arithmetic(building.level, building.building_element.people_storage)
        city.civilization_value += building.building_element.civilization_value
        city.save()
        # 删除升级序列
        improving_building.delete()
        sleep += 1
        if sleep%100 == 0: time.sleep(1)

    del now, city, building, improving_building_list
    time.sleep(1)

    # 专家升级
    now = datetime.datetime.now(); professional = Professional()
    improving_professional_list = ImprovingProfessional.objects.filter(end_time__lt = now)
    for improving_professional in improving_professional_list:
        # 建筑升级/建造完成
        professional = improving_professional.professional
        professional.level = improving_professional.level
        professional.save()
        # 改变城市数值
        #city = update_resources(building.city.id, now)
        #city.food_speed += level_arithmetic(building.level, building.building_element.food_speed)
        #city.food_storage += level_arithmetic(building.level, building.building_element.food_storage)
        #city.wood_speed += level_arithmetic(building.level, building.building_element.wood_speed)
        #city.wood_storage += level_arithmetic(building.level, building.building_element.wood_storage)
        #city.ore_speed += level_arithmetic(building.level, building.building_element.ore_speed)
        #city.ore_storage += level_arithmetic(building.level, building.building_element.ore_storage)
        #city.gold_storage += level_arithmetic(building.level, building.building_element.gold_storage)
        #city.people_storage += level_arithmetic(building.level, building.building_element.people_storage)
        #city.civilization_value += building.building_element.civilization_value
        #city.save()
        # 删除升级序列
        improving_professional.delete()
        sleep += 1
        if sleep%100 == 0: time.sleep(1)

    del now, professional, improving_professional_list
    time.sleep(1)


