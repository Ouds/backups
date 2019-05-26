# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/member/views/build_upgrade.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: views file of member module.
#===============================================================================

import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from ouds.city.models import City, BuildingElement

#===============================================================================
# 为点击位置取得可建建筑
#===============================================================================

@login_required
def city(request, template_name = 'city/layout.ouds'):
    '''城市布局图'''

    user = request.user
    profile = user.get_profile()

    # 城市切换
    if 'city_id' in request.POST:
        city_id = request.POST['city_id']
        city_list = profile.city_set.all()
        city_ids = []
        for city in city_list:
            city_ids.append(city.id)
        if city_id in city_ids:
            city = City.objects.get(id = city_id)
        else:
            return HttpResponseRedirect('/member/warning')
    # 会话
    elif 'city_id' in request.session:
        city_id = request.session['city_id']
        city = City.objects.get(id = city_id)
    # 登录
    else:
        city = profile.city_set.get(is_capital = True)

    request.session['city_id'] = city.id
    building_list = city.building_set.all()

    return render_to_response(
            template_name,
            {
                'user': user,
                'city': city,
                'building_list': building_list,
               },
           )

#===============================================================================
# 为点击位置取得可建建筑
#===============================================================================

from ouds.city.models import ForceElement

@login_required
def location(request, template_name = 'city/location.ouds'):
    '''可建在此位置的建筑'''

    if request.method != 'POST':
        return HttpResponseRedirect('/city')
    
    user = request.user
    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    location = int(request.POST['location'])

    building_element_list = []
    # 皇宫/府衙
    if location == 0:
        if city.is_capital:
            building_element_list.append(BuildingElement.objects.get(id = 1))
        else:
            building_element_list.append(BuildingElement.objects.get(id = 2))

    # 城内建筑
    if 1 <= location <= 19:
        # 兵部
        if location == 1:
            if user.get_profile().type == 1: # 武型玩家建立兵部
                building_element_list.append(BuildingElement.objects.get(id = 3))
        
        # 船坞
        if location == 2:
            coordinate = city.coordinate
            latitude = coordinate.latitude
            longitude = coordinate.longitude
            from ouds.map.models import Coordinate
            property_list = Coordinate.objects.filter(latitude__range = (latitude - 1, latitude + 1), \
                    longitude__range = (longitude - 1, longitude + 1)).values_list('property')
            if (0,) in property_list or (9,) in property_list: # 0：水域；9：运河，可建立船坞
                building_element_list.append(BuildingElement.objects.get(id = 4))
        
        building_element_set = BuildingElement.objects.filter(id__range = (5, 33))
        for building_element in building_element_set:
            if city.is_capital:
                building_element_list.append(building_element)
            elif building_element.id != 20: # 非首都没有鸿泸寺
                building_element_list.append(building_element)
            
        building_set = city.building_set.filter(building_element__range = (5, 33))
        for building in building_set:
            for o in xrange(len(building_element_list)):
                if building_element_list[o] == building.building_element:
                    del building_element_list[o]
                    break

    # 资源
    if 24 <= location <= 35:
        building_element_list = BuildingElement.objects.filter(id__range = (34, 36))

    return render_to_response(
            template_name,
            {
            'user': user,
            'city': city,
            'location': location,
            'building_element_list': building_element_list,
            },
           )

#===============================================================================
# 在某一位置建造建筑
#===============================================================================

from ouds.utils.comms import _md5
from ouds.city.models import Building, ImprovingBuilding

@login_required
def location_build(request):
    '''在某一位置建造建筑'''

    if request.method != 'POST':
        return HttpResponseRedirect('/city')

    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    location = request.POST['location']
    if city.building_set.filter(location = location):
        return HttpResponseRedirect('/member/warning')

    # 得到建筑元素、城市信息
    building_element = BuildingElement.objects.get(id = request.POST['building_element_id'])

    # 改变城市资源、狗，以及马数值
    city.food -= building_element.food
    city.wood -= building_element.wood
    city.ore -= building_element.ore
    city.gold -= building_element.gold
    city.people -= building_element.people
    city.save()

    use_dog = building_element.dog
    if use_dog > 0:
        dog = city.force_set.filter(force_element = ForceElement(id = 1))[0]
        dog.amount -= use_dog
        dog.save()
    
    use_horse = building_element.horse
    if use_horse > 0:
        horse = city.force_set.filter(force_element = ForceElement(id = 2))[0]
        horse.amount -= use_horse
        horse.save()
    
    # 当前时间
    now = datetime.datetime.now()
    
    # 建造建筑
    building = Building()
    building.id = _md5(request.user.username, now)
    building.city = city
    building.building_element = building_element
    building.location = location
    building.level = 0
    building.save()

    # 加入升级序列
    improving_building = ImprovingBuilding()
    improving_building.id = _md5(request.user.username, now)
    improving_building.city = city
    improving_building.building = building
    improving_building.level = 1
    latest_time = now
    if city.improvingbuilding_set.count():
        latest_time = city.improvingbuilding_set.latest('end_time').end_time
        if latest_time < now: latest_time = now
    improving_building.end_time = latest_time + datetime.timedelta(seconds = building_element.time)
    improving_building.save()

    return HttpResponse('to /city')

################1#####################

@login_required
def building(request, id, template_name = 'city/building.ouds'):
    '''建筑信息'''
    
    if not request.session.has_key('city_id'):
        return HttpResponseRedirect('/city')
    
    user = request.user
    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    building = city.building_set.get(id = id)
    
    return render_to_response(
            template_name,
            {
                'user': user,
                'city': city,
                'building': building,
               },
           )

#===============================================================================
# 升级某建筑
#===============================================================================

from ouds.utils.templatetags.read import level_arithmetic

@login_required
def building_improve(request):
    '''升级某建筑'''
    
    if request.method != 'POST':
        return HttpResponseRedirect('/city')
    
    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    building = Building.objects.get(id = request.POST['id'])
    level = building.level + building.improvingbuilding_set.count() + 1

    # 改变城市资源、狗，以及马数值
    city.food -= level_arithmetic(level, building.building_element.food)
    city.wood -= level_arithmetic(level, building.building_element.wood)
    city.ore -= level_arithmetic(level, building.building_element.ore)
    city.gold -= level_arithmetic(level, building.building_element.gold)
    city.people -= level_arithmetic(level, building.building_element.people)
    city.save()

    use_dog = level_arithmetic(level, building.building_element.dog)
    if use_dog > 0:
        dog = city.force_set.filter(force_element = ForceElement(id = 1))[0]
        dog.amount -= use_dog
        dog.save()

    use_horse = level_arithmetic(level, building.building_element.horse)
    if use_horse > 0:
        horse = city.force_set.filter(force_element = ForceElement(id = 2))[0]
        horse.amount -= use_horse
        horse.save()

    # 当前时间
    now = datetime.datetime.now()

    # 加入升级序列
    improving_building = ImprovingBuilding()
    improving_building.id = _md5(request.user.username, now)
    improving_building.city = city
    improving_building.building = building
    improving_building.level = level
    latest_time = now
    if city.improvingbuilding_set.count():
        latest_time = city.improvingbuilding_set.latest('end_time').end_time
        if latest_time < now: latest_time = now
    improving_building.end_time = latest_time + datetime.timedelta(seconds = level_arithmetic(level, building.building_element.time))
    improving_building.save()
    
    return HttpResponse('reload')

###########训练专家##########

from ouds.city.models import ProfessionalElement, Professional, ImprovingProfessional, WareElement

@login_required
def professional_educate(request):
    """训练专家"""
    
    if request.method != 'POST':
        return HttpResponseRedirect('/city')

    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    
    professional_element = ProfessionalElement.objects.get(id = request.POST['professional_element_id'])

    # 改变城市黄金、物资、狗，以及马数值
    city.gold -= professional_element.gold;
    city.save()

    if not int(request.POST['is_first']):
        city_ware = city.ware_set

        mu_qi = city_ware.get(ware_element = WareElement(id = 1))
        mu_qi.amount -= professional_element.mu_qi
        mu_qi.save()
        
        ci_qi = city_ware.get(ware_element = WareElement(id = 6))
        ci_qi.amount -= professional_element.ci_qi
        ci_qi.save()
        
        jiu_shui = city_ware.get(ware_element = WareElement(id = 11))
        jiu_shui.amount -= professional_element.jiu_shui
        jiu_shui.save()
        
        yu_qi = city_ware.get(ware_element = WareElement(id = 16))
        yu_qi.amount -= professional_element.yu_qi
        yu_qi.save()

        use_dog = professional_element.dog
        if use_dog > 0:
            dog = city.force_set.filter(force_element = ForceElement(id = 1))[0]
            dog.amount -= use_dog
            dog.save()
        
        use_horse = professional_element.horse
        if use_horse > 0:
            horse = city.force_set.filter(force_element = ForceElement(id = 2))[0]
            horse.amount -= use_horse
            horse.save()
    
    # 当前时间
    now = datetime.datetime.now()

    # 培养专家
    professional = Professional()
    professional.id = _md5(request.user.username, now)
    professional.name = request.POST['name']
    professional.building = Building(id = request.POST['building_id'])
    professional.professional_element = professional_element
    professional.health = 100
    professional.intelligence = 0
    professional.powers = 0
    professional.loyalty = 100
    professional.leadership = 0
    professional.skills = 0
    professional.level = 0
    professional.save()

    # 加入升级序列
    improving_professional = ImprovingProfessional()
    improving_professional.id = _md5(request.user.username, now)
    improving_professional.city = city
    improving_professional.professional = professional
    improving_professional.level = 1
    improving_professional.end_time = now + datetime.timedelta(seconds = professional_element.time)
    improving_professional.save()

    return HttpResponse('reload')


###########升级专家##########

from ouds.utils.templatetags.read import element_level, ware_element_id, professional_increment

@login_required
def professional_improve(request):
    '''专家升级'''

    if request.method != 'POST':
        return HttpResponseRedirect('/city')

    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    professional = Professional.objects.get(id = request.POST['id'])
    level = professional.level + professional.improvingprofessional_set.count() + 1
    
    # 改变城市黄金、狗、马数值
    city.gold -= level_arithmetic(level, professional.professional_element.gold)
    city.save()
    
    use_dog = level_arithmetic(level, professional.professional_element.dog)
    if use_dog > 0:
        dog = city.force_set.filter(force_element = ForceElement(id = 1))[0]
        dog.amount -= use_dog
        dog.save()
    
    use_horse = level_arithmetic(level, professional.professional_element.horse)
    if use_horse > 0:
        horse = city.force_set.filter(force_element = ForceElement(id = 2))[0]
        horse.amount -= use_horse
        horse.save()
    
    # 判断需要那种城市物资，并改变数值
    pi = professional_increment(level)
    ware_level = element_level(level)
    city_ware = city.ware_set

    mu_qi = city_ware.get(ware_element = WareElement(id = ware_element_id(ware_level, 'mu-qi')))
    mu_qi.amount -= level_arithmetic(pi, professional.professional_element.mu_qi)
    mu_qi.save()

    ci_qi = city_ware.get(ware_element = WareElement(id = ware_element_id(ware_level, 'ci-qi')))
    ci_qi.amount -= level_arithmetic(pi, professional.professional_element.ci_qi)
    ci_qi.save()
    
    jiu_shui = city_ware.get(ware_element = WareElement(id = ware_element_id(ware_level, 'jiu-shui')))
    jiu_shui.amount -= level_arithmetic(pi, professional.professional_element.jiu_shui)
    jiu_shui.save()
    
    yu_qi = city_ware.get(ware_element = WareElement(id = ware_element_id(ware_level, 'yu-qi')))
    yu_qi.amount -= level_arithmetic(pi, professional.professional_element.yu_qi)
    yu_qi.save()

    # 当前时间
    now = datetime.datetime.now()

    # 加入升级序列
    improving_professional = ImprovingProfessional()
    improving_professional.id = _md5(request.user.username, now)
    improving_professional.city = city
    improving_professional.professional = professional
    improving_professional.level = level
    latest_time = now
    if professional.improvingprofessional_set.count():
        latest_time = professional.improvingprofessional_set.latest('end_time').end_time
        if latest_time < now: latest_time = now
    improving_professional.end_time = latest_time + datetime.timedelta(seconds = level_arithmetic(level, professional.professional_element.time))
    improving_professional.save()

    return HttpResponse('reload')


