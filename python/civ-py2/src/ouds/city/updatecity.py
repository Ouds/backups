# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/common/comms.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: common files.
#===============================================================================

from ouds.city.models import City

def update_resources(city_id, now):
    '''modify resource'''
    
    city = City.objects.get(id = city_id)
    
    # food
    food_time = now - city.food_updated; food_days = food_time.days; food_seconds = food_time.seconds
    food_speed = city.food_speed; food = city.food; food_storage = city.food_storage
    food_increment = food_speed * (food_days * 24 + food_seconds / 3600)
    if food_increment > 0:
        food += food_increment
        if food > food_storage: food = food_storage
        city.food = food
        city.food_updated = now

    # wood
    wood_time = now - city.wood_updated; wood_days = wood_time.days; wood_seconds = wood_time.seconds
    wood_speed = city.wood_speed; wood = city.wood; wood_storage = city.wood_storage
    wood_increment = wood_speed * (wood_days * 24 + wood_seconds / 3600)
    if wood_increment > 0:
        wood += wood_increment
        if wood > wood_storage: wood = wood_storage
        city.wood = wood
        city.wood_updated = now

    # ore
    ore_time = now - city.ore_updated; ore_days = ore_time.days; ore_seconds = ore_time.seconds
    ore_speed = city.ore_speed; ore = city.ore; ore_storage = city.ore_storage
    ore_increment = ore_speed * (ore_days * 24 + ore_seconds / 3600)
    if ore_increment > 0:
        ore += ore_increment
        if ore > ore_storage: ore = ore_storage
        city.ore = ore
        city.ore_updated = now

    # people
    people_time = now - city.people_updated; people_days = people_time.days; people_seconds = people_time.seconds
    people = city.people; people_storage = city.people_storage
    people_increment = city.civilization_value * (people_days * 24 + people_seconds / 3600)
    if people_increment > 0:
        people += people_increment
        if people > people_storage: people = people_storage
        city.people = people
        city.people_updated = now
    
    # gold
    gold_time = now - city.gold_updated; gold_days = gold_time.days; gold_seconds = gold_time.seconds
    gold = city.gold; gold_storage = city.gold_storage
    gold_increment = (people / 100) * (gold_days * 24 + gold_seconds / 3600)
    if gold_increment > 0:
        gold += gold_increment
        if gold > gold_storage: gold = gold_storage
        city.gold = gold
        city.gold_updated = now

    city.save()
    return city

