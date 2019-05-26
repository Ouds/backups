# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/map/models.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: models file of map module.
#===============================================================================

from django.db import models
from django.utils.translation import ugettext_lazy as _

#=========================================================
# 坐标信息
#=========================================================

from ouds.utils.CONSTANT import COORDINATE_PROPERTY

class Coordinate(models.Model):
    '''坐标基本特征描述'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    longitude = models.IntegerField(_(u'经度'), db_index = True)
    latitude = models.IntegerField(_(u'纬度'), db_index = True)
    altitude = models.IntegerField(_(u'海拔'), db_index = True)
    property = models.PositiveSmallIntegerField(_(u'属性'), choices = COORDINATE_PROPERTY, db_index = True)

    food_parameter = models.DecimalField(_(u'粮食参数'), max_digits = 3, decimal_places = 2)
    wood_parameter = models.DecimalField(_(u'木头参数'), max_digits = 3, decimal_places = 2)
    ore_parameter = models.DecimalField(_(u'矿类参数'), max_digits = 3, decimal_places = 2)
    people_parameter = models.DecimalField(_(u'人口参数'), max_digits = 3, decimal_places = 2)

    class Meta:
        verbose_name = _(u'坐标特征')
        verbose_name_plural = _(u'坐标特征')
        unique_together = ('longitude', 'latitude')

    def __unicode__(self):
        return u'(%s, %s, %s) %s' % (self.longitude, self.latitude, self.altitude, COORDINATE_PROPERTY[self.property][1])

