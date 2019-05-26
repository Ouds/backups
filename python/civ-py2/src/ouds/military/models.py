# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@ouds.us
# Project: Civilization 
# File Name: ouds/city/models.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: models file of city module.
#===============================================================================

from django.db import models
from django.utils.translation import ugettext_lazy as _

####################################

from ouds.utils.consts import GENERAL_TYPE

class General(models.Model):
    '''将领信息'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    name = models.CharField(_(u'名字'), max_length = 50)
    type = models.SmallIntegerField(_(u'类型'), choices = GENERAL_TYPE)
    level = models.PositiveSmallIntegerField(_(u'级别'))
    health = models.PositiveSmallIntegerField(_(u'血量'))
    
    tongyu = models.PositiveIntegerField(_(u'统御'))
    jineng = models.PositiveIntegerField(_(u'技能'))
    wuli = models.PositiveIntegerField(_(u'武力'))

    class Meta:
        verbose_name = _(u'将领信息')
        verbose_name_plural = _(u'将领信息')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.type)


##################################

from ouds.member.models import TechElement

class Force(models.Model):
    '''武力详细信息描述'''
    
    name = models.CharField(_(u'名字'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    food = models.IntegerField(_(u'粮食消耗元量'))
    wood = models.IntegerField(_(u'木头消耗元量'))
    ore = models.IntegerField(_(u'矿物消耗元量'))
    gold = models.IntegerField(_(u'黄金消耗元量'))
    time = models.SmallIntegerField(_(u'时间元量/秒'))
    tech_element = models.ManyToManyField(TechElement, verbose_name = _(u'科技基础'), blank = True)
    restraint = models.ManyToManyField('self', verbose_name = _(u'克制'), null = True, blank = True)

    class Meta:
        verbose_name = _(u'武力元素')
        verbose_name_plural = _(u'武力元素')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.time)

##################################

from ouds.member.models import TechElement

class Wushu(models.Model):
    '''强身搏击术'''
    
    name = models.CharField(_(u'名字'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    weapon = models.BooleanField(_(u'需要武器'))
    nei_li = models.PositiveSmallIntegerField(_(u'内功元量'))
    wei_li = models.PositiveSmallIntegerField(_(u'外力元量'))
    an_qi = models.PositiveSmallIntegerField(_(u'暗算元量'))
    gold = models.IntegerField(_(u'黄金消耗元量'))
    time = models.SmallIntegerField(_(u'时间元量/秒'))
    tech_element = models.ManyToManyField(TechElement, verbose_name = _(u'科技基础'), blank = True)
    restraint = models.ManyToManyField('self', verbose_name = _(u'克制'), blank = True)

    class Meta:
        verbose_name = _(u'强身搏击术')
        verbose_name_plural = _(u'强身搏击术')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.time)

