# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/simulator/views.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: views file of member module.
#===============================================================================

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

##########################

from ouds.city.models import City
from ouds.simulator.forms import MetaForm

@login_required
def level_count(request, meta_form = MetaForm, template_name = 'simulator/level_count.ouds'):
    '''根据元量计算级别总量'''

    user = request.user
    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    dict = {
            'user': user,
            'city': city,
            }

    if request.method == 'GET':
        meta_form = meta_form(auto_id = False)
        dict.update(meta_form = meta_form, levels = xrange(0))
    elif request.method == 'POST':
        post = request.POST
        meta_form = meta_form(post, auto_id = False)
        dict.update(meta_form = meta_form)
        if meta_form.is_valid():
            dict.update(meta = int(post['meta']), levels = xrange(1, 46))
        else:
            dict.update(meta = post['meta'], levels = xrange(0))
        
    return render_to_response(
            template_name,
            dict,
           )


