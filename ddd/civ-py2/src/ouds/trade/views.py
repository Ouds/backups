# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/member/views.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: views file of member module.
#===============================================================================

from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

from ouds.city.models import City
from ouds.map.models import Coordinate

#===============================================================================
# 游戏地图
#===============================================================================

from ouds.utils.consts import MARGIN_ROWS, MARGIN_COLUMNS
from ouds.map.forms import CoordinateForm

@login_required
def map(request, coordinate_form = CoordinateForm, template_name = 'map/map.ouds'):
    '''城市地图'''

    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    longitude = city.coordinate.longitude; latitude = city.coordinate.latitude

    if request.method == 'POST':
        post = request.POST
        coordinate_form = coordinate_form(post, auto_id = False)
        if coordinate_form.is_valid():
            longitude = int(post['longitude']); latitude = int(post['latitude'])
    else:
        if request.GET:
            get = request.GET
            longitude = int(get['longitude']) + int(get['lm']) * MARGIN_ROWS; latitude = int(get['latitude']) + int(get['tm']) * MARGIN_COLUMNS
        coordinate_form = coordinate_form({'longitude': longitude, 'latitude': latitude}, auto_id = False)

    coordinate = Coordinate.objects.get(longitude = longitude, latitude = latitude)
    left = longitude - MARGIN_ROWS; right = longitude + MARGIN_ROWS
    top = latitude + MARGIN_COLUMNS; bottom = latitude - MARGIN_COLUMNS
    coordinate_rows = []
    for lat in xrange(top, bottom-1, -1):
        coordinate_row = Coordinate.objects.filter(longitude__range = (left, right), latitude = lat)
        coordinate_rows.append(coordinate_row)

    return render_to_response(
            template_name,
            {
                'user': request.user,
                'city': city,
                'coordinate_form': coordinate_form,
                'coordinate': coordinate,
                'coordinate_rows': coordinate_rows,
               },
           )

######################################

@login_required
def coordinate(request, coordinate_id, template_name = 'map/coordinate.ouds'):
    '''由地图查看城市信息'''

    city_id = request.session['city_id']
    city = City.objects.get(id = city_id)
    coordinate = Coordinate.objects.get(id = coordinate_id)

    return render_to_response(
            template_name,
            {
                'user': request.user,
                'city': city,
                'coordinate': coordinate,
               },
           )


