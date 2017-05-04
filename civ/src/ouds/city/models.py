# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/city/models.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: models file of city module.
#===============================================================================

from django.db import models
from django.utils.translation import ugettext_lazy as _

#=========================================================
# 城市信息
#=========================================================

class CityManager(models.Manager):
    '''新城管理器'''
    
    def create_city(self, now, id, profile, coordinate, name = _(u'新城'), is_capital = False, era = u'forest', \
            food_speed = 0, food = 1000, food_storage = 1000, \
            wood_speed = 0, wood = 1000, wood_storage = 1000, \
            ore_speed = 0, ore = 1000, ore_storage = 1000, \
            gold = 1000, gold_storage = 1000, people = 108, people_storage = 108, civilization_value = 0):
        
        return self.create(id = id, profile = profile, coordinate = coordinate, name = name, is_capital = is_capital , era = era, \
                food_speed = food_speed, food = food, food_storage = food_storage, food_updated = now, \
                wood_speed = wood_speed, wood = wood, wood_storage = wood_storage, wood_updated = now, \
                ore_speed = ore_speed, ore = ore, ore_storage = ore_storage, ore_updated = now, \
                gold = gold, gold_storage = gold_storage, gold_updated = now, \
                people = people, people_storage = people_storage, people_updated = now, \
                civilization_value = civilization_value)

##################################

from ouds.member.models import Profile
from ouds.map.models import Coordinate

class City(models.Model):
    '''城市基本信息描述'''

    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    profile = models.ForeignKey(Profile, verbose_name = _(u'用户'), null = True, blank = True)
    coordinate = models.OneToOneField(Coordinate, verbose_name = _(u'坐标'))
    name = models.CharField(_(u'城名'), max_length = 26, db_index = True)
    is_capital = models.BooleanField(_(u'首都'))
    season = models.CharField(_(u'季节'), max_length = 6, default = 'spring', db_index = True)
    era = models.CharField(_(u'城市纪元'), max_length = 6, default = 'forest', db_index = True)
    status = models.SmallIntegerField(_(u'城市状况'), default = 0, db_index = True)
    catastrophe = models.SmallIntegerField(_(u'灾祸'), default = 0, db_index = True)

    food_speed = models.PositiveIntegerField(_(u'粮食产量'))
    food = models.PositiveIntegerField(_(u'粮食存量'))
    food_storage = models.PositiveIntegerField(_(u'粮仓容量'))
    food_updated = models.DateTimeField(_(u'粮食更新时间'))
    
    wood_speed = models.PositiveIntegerField(_(u'木材产量'))
    wood = models.PositiveIntegerField(_(u'木材存量'))
    wood_storage = models.PositiveIntegerField(_(u'木库容量'))
    wood_updated = models.DateTimeField(_(u'木材更新时间'))

    ore_speed = models.PositiveIntegerField(_(u'矿类产量'))
    ore = models.PositiveIntegerField(_(u'矿类存量'))
    ore_storage = models.PositiveIntegerField(_(u'矿库容量'))
    ore_updated = models.DateTimeField(_(u'矿类更新时间'))
    
    gold = models.PositiveIntegerField(_(u'黄金现量'))
    gold_storage = models.PositiveIntegerField(_(u'金库容量'))
    gold_updated = models.DateTimeField(_(u'税收更新时间'))
    
    people = models.PositiveIntegerField(_(u'人口现数'))
    people_storage = models.PositiveIntegerField(_(u'城市容量'))
    people_updated = models.DateTimeField(_(u'人口更新时间'))

    civilization_value = models.PositiveIntegerField(_(u'文明度'), db_index = True)
    
    objects = CityManager()

    class Meta:
        verbose_name = _(u'城市信息')
        verbose_name_plural = _(u'城市信息')
        unique_together = ('profile', 'name')
        ordering = ['-civilization_value']

    def __unicode__(self):
        return u'%s %s %s %s' % (self.profile, self.coordinate, self.name, self.civilization_value)

#=========================================================
# 建筑元素信息
#=========================================================

from ouds.member.models import TechElement

class BuildingElement(models.Model):
    '''建筑元素信息描述'''
    
    name = models.CharField(_(u'名称'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    tech_element = models.ManyToManyField(TechElement, verbose_name = _(u'科技基础'), blank = True)
    
    food = models.PositiveSmallIntegerField(_(u'粮食消耗元量'))
    food_speed = models.PositiveSmallIntegerField(_(u'粮食增量元量'))
    food_storage = models.PositiveSmallIntegerField(_(u'粮仓容量元量'))
    
    wood = models.PositiveSmallIntegerField(_(u'木头消耗元量'))
    wood_speed = models.PositiveSmallIntegerField(_(u'木材增量元量'))
    wood_storage = models.PositiveSmallIntegerField(_(u'木棚容量元量'))

    ore = models.PositiveSmallIntegerField(_(u'矿物消耗元量'))
    ore_speed = models.PositiveSmallIntegerField(_(u'矿类增量元量'))
    ore_storage = models.PositiveSmallIntegerField(_(u'矿库容量元量'))

    dog = models.PositiveSmallIntegerField(_(u'狗元量'))
    horse = models.PositiveSmallIntegerField(_(u'马元量'))
    
    gold = models.PositiveSmallIntegerField(_(u'黄金消耗元量'))
    gold_storage = models.PositiveSmallIntegerField(_(u'金库容量元量'))

    people = models.PositiveSmallIntegerField(_(u'人口消耗元量'))
    people_storage = models.PositiveSmallIntegerField(_(u'城市容量元量'))

    time = models.PositiveSmallIntegerField(_(u'时间元量/秒'))
    civilization_value = models.PositiveSmallIntegerField(_(u'文明点数'), editable = False, db_index = True)

    class Meta:
        verbose_name = _(u'建筑元素')
        verbose_name_plural = _(u'建筑元素')
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.name, self.civilization_value)

#=========================================================
# 建筑信息
#=========================================================

class Building(models.Model):
    '''城市建筑信息描述'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    city = models.ForeignKey(City, verbose_name = _(u'城市信息'))
    building_element = models.ForeignKey(BuildingElement, verbose_name = _(u'建筑元素'))
    location = models.PositiveSmallIntegerField(_(u'位置'))
    level = models.PositiveSmallIntegerField(_(u'当前级别'))

    class Meta:
        verbose_name = _(u'建筑信息')
        verbose_name_plural = _(u'建筑信息')
        unique_together = ('city', 'location')
        ordering = ['city']

    def __unicode__(self):
        return u'%s %s %s' % (self.city, self.building_element.name, self.level)

##########################################

class ImprovingBuilding(models.Model):
    '''城市中正在升级的建筑信息描述'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    city = models.ForeignKey(City, verbose_name = _(u'城市信息'))
    building = models.ForeignKey(Building, verbose_name = _(u'建筑信息'))
    level = models.PositiveSmallIntegerField(_(u'升级级别'))
    end_time = models.DateTimeField(_(u'完成时间'), db_index = True)

    class Meta:
        verbose_name = _(u'升级中建筑')
        verbose_name_plural = _(u'升级中建筑')
        unique_together = ('city', 'building', 'level')
        ordering = ['end_time']

    def __unicode__(self):
        return u'%s %s %s' % (self.building, self.level, self.end_time)

###########################################

class ProfessionalElement(models.Model):
    '''专家元素'''
    
    name = models.CharField(_(u'专业'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    building_element = models.ForeignKey(BuildingElement, verbose_name = _(u'归属单位'))
    mu_qi = models.PositiveSmallIntegerField(_(u'木器元量'))
    ci_qi = models.PositiveSmallIntegerField(_(u'瓷器元量'))
    jiu_shui = models.PositiveSmallIntegerField(_(u'酒水元量'))
    yu_qi = models.PositiveSmallIntegerField(_(u'玉器元量'))
    dog = models.PositiveSmallIntegerField(_(u'狗狗元量'))
    horse = models.PositiveSmallIntegerField(_(u'马匹元量'))
    gold = models.PositiveSmallIntegerField(_(u'黄金元量'))
    time = models.PositiveSmallIntegerField(_(u'时间元量/秒'))

    class Meta:
        verbose_name = _(u'专家元素')
        verbose_name_plural = _(u'专家元素')
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.name, self.building_element.name, self.time)

#######################################

class Professional(models.Model):
    '''专家信息'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    name = models.CharField(_(u'名号'), max_length = 50, db_index = True)
    building = models.ForeignKey(Building, verbose_name = _(u'所属建筑'))
    professional_element = models.ForeignKey(ProfessionalElement, verbose_name = _(u'专家元素'))
    health = models.PositiveSmallIntegerField(_(u'生命力'))
    intelligence = models.PositiveSmallIntegerField(_(u'智商'))
    powers = models.PositiveSmallIntegerField(_(u'力量'))
    loyalty = models.PositiveSmallIntegerField(_(u'忠诚度'))
    leadership = models.PositiveSmallIntegerField(_(u'统御力'))
    skills = models.PositiveSmallIntegerField(_(u'技能值'))
    level = models.PositiveSmallIntegerField(_(u'专家级别'))

    class Meta:
        verbose_name = _(u'专家信息')
        verbose_name_plural = _(u'专家信息')
        ordering = ['-level']

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.name, self.building.city.name, self.building.building_element.name, self.professional_element.name, self.level)

########################################

class ImprovingProfessional(models.Model):
    '''城市中正在升级的专家'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    professional = models.ForeignKey(Professional, verbose_name = _(u'专家信息'))
    level = models.PositiveSmallIntegerField(_(u'升级级别'))
    end_time = models.DateTimeField(_(u'完成时间'), db_index = True)

    class Meta:
        verbose_name = _(u'升级中专家')
        verbose_name_plural = _(u'升级中专家')
        unique_together = ('professional', 'level')
        ordering = ['end_time']

    def __unicode__(self):
        return u'%s %s %s' % (self.professional, self.level, self.end_time)

##################################

class WareElement(models.Model):
    '''物件元素'''

    name = models.CharField(_(u'名称'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    building_element = models.ForeignKey(BuildingElement, verbose_name = _(u'生产单位'))
    level = models.PositiveSmallIntegerField(_(u'生产级别'))
    food = models.PositiveSmallIntegerField(_(u'粮食元量'))
    wood = models.PositiveSmallIntegerField(_(u'木头元量'))
    ore = models.PositiveSmallIntegerField(_(u'矿物元量'))
    gold = models.PositiveSmallIntegerField(_(u'黄金元量'))
    time = models.PositiveSmallIntegerField(_(u'时间元量/秒'))

    class Meta:
        verbose_name = _(u'物件元素')
        verbose_name_plural = _(u'物件元素')
        ordering = ['id', 'building_element']

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.name, self.building_element.name, self.level)

#######################################

class Ware(models.Model):
    '''物件信息'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    city = models.ForeignKey(City, verbose_name = _(u'城市信息'))
    ware_element = models.ForeignKey(WareElement, verbose_name = _(u'物件元素'))
    amount = models.PositiveIntegerField(_(u'数量'))

    class Meta:
        verbose_name = _(u'物件信息')
        verbose_name_plural = _(u'物件信息')
        unique_together = ('city', 'ware_element')

    def __unicode__(self):
        return u'%s %s %s' % (self.city.name, self.ware_element.name, self.amount)

########################################

class ProducingWare(models.Model):
    '''正在生产的物件'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    ware = models.ForeignKey(Ware, verbose_name = _(u'物件信息'))
    professional = models.ForeignKey(Professional, verbose_name = _(u'专家信息'))
    amount = models.PositiveIntegerField(_(u'生产数量'))
    updated_time = models.DateTimeField(_(u'更新时间'), db_index = True)
    is_stopped = models.PositiveSmallIntegerField(_(u'是否停止'))

    class Meta:
        verbose_name = _(u'生产中物件')
        verbose_name_plural = _(u'生产中物件')
        unique_together = ('ware', 'professional')
        ordering = ['updated_time']

    def __unicode__(self):
        return u'%s %s %s' % (self.ware, self.professional.name, self.is_stopped)

###################################

class ForceElement(models.Model):
    '''武力元素'''

    name = models.CharField(_(u'名称'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    building_element = models.ForeignKey(BuildingElement, verbose_name = _(u'培训单位'))
    level = models.PositiveSmallIntegerField(_(u'武力级别'))
    speed = models.PositiveSmallIntegerField(_(u'速度'))
    food = models.PositiveSmallIntegerField(_(u'粮食元量'))
    wood = models.PositiveSmallIntegerField(_(u'木头元量'))
    ore = models.PositiveSmallIntegerField(_(u'矿物元量'))
    gold = models.PositiveSmallIntegerField(_(u'黄金元量'))
    time = models.PositiveSmallIntegerField(_(u'时间元量/秒'))
    restraint = models.ManyToManyField('self', verbose_name = _(u'克制'), symmetrical = False, blank = True)

    class Meta:
        verbose_name = _(u'武力元素')
        verbose_name_plural = _(u'武力元素')
        ordering = ['id']
    
    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.name, self.building_element.name, self.level)

#######################################

class Force(models.Model):
    '''武力信息'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    city = models.ForeignKey(City, verbose_name = _(u'城市信息'))
    professional = models.ForeignKey(Professional, verbose_name = _(u'本部统帅'), null = True, blank = True)
    force_element = models.ForeignKey(ForceElement, verbose_name = _(u'武力元素'))
    amount = models.PositiveIntegerField(_(u'数量'))

    class Meta:
        verbose_name = _(u'武力信息')
        verbose_name_plural = _(u'武力信息')
        unique_together = ('professional', 'force_element')
        ordering = ['city']

    def __unicode__(self):
        return u'%s %s %s %s' % (self.city.name, self.professional, self.force_element.name, self.amount)

########################################

class TrainingForce(models.Model):
    '''正在训练的武力'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    force = models.ForeignKey(Force, verbose_name = _(u'武力信息'), unique = True)
    amount = models.PositiveIntegerField(_(u'训练数量'))
    updated_time = models.DateTimeField(_(u'更新时间'), db_index = True)
    is_stopped = models.PositiveSmallIntegerField(_(u'是否停止'))

    class Meta:
        verbose_name = _(u'训练中武力')
        verbose_name_plural = _(u'训练中武力')
        ordering = ['updated_time']

    def __unicode__(self):
        return u'%s %s %s' % (self.force, self.force.professional.name, self.is_stopped)



