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

#################

from ouds.utils.CONSTANT import COORDINATE_PROPERTY

class Sell(models.Model):
    '''售出信息'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    amount = models.PositiveIntegerField(_(u'数量'))

    class Meta:
        verbose_name = _(u'售出信息')
        verbose_name_plural = _(u'售出信息')

    def __unicode__(self):
        return u'%s %s %s' % (self.longitude, self.latitude, COORDINATE_PROPERTY[self.property][1])

