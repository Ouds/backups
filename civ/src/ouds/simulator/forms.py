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

class MetaForm(forms.Form):
    """元量"""
    
    meta = forms.IntegerField(label = _(u'元量'), min_value = 1)

