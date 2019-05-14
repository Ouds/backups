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

import datetime

from ouds.map.models import Coordinate

#=========================================================
# 写入所有坐标
#=========================================================

start_time = datetime.datetime.now()
print start_time

for o in range(-988, -887):
    for d in range(-50, 51):
        coordinate = Coordinate()
        coordinate.id = str(o) + '_' + str(d)
        coordinate.longitude = o
        coordinate.latitude = d
        coordinate.altitude = 1000
        coordinate.property = 7
        coordinate.water_parameter = 1
        coordinate.food_parameter = 1
        coordinate.wood_parameter = 1
        coordinate.clay_stone_parameter = 1
        coordinate.ore_parameter = 1
        coordinate.people_parameter = 1
        coordinate.save()
        d += 1
    print coordinate.longitude, coordinate.latitude
    o += 1

end_time = datetime.datetime.now()
print end_time

print end_time - start_time



