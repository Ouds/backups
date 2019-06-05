# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/auth/forms.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: forms file of auth module.
#===============================================================================

from django import forms
from django.utils.translation import ugettext_lazy as _

from ouds.utils.consts import MIN_LONGITUDE, MAX_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE

class CoordinateForm(forms.Form):
    """调整坐标中心"""
    
    longitude = forms.IntegerField(label = _(u'经度'), min_value = MIN_LONGITUDE, max_value = MAX_LONGITUDE, widget = forms.TextInput(attrs = {'size': '3', 'maxlength': '6', 'style': 'text-align:center'}))
    latitude = forms.IntegerField(label = _(u'纬度'), min_value = MIN_LATITUDE, max_value = MAX_LATITUDE, widget = forms.TextInput(attrs = {'size': '3', 'maxlength': '6', 'style': 'text-align:center'}))

