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

import datetime

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

from ouds.utils.comms import _paginator_dict

from cStringIO import StringIO
from random import randint, choice

from PIL import Image, ImageDraw, ImageFont

from ouds.member import captcha
from ouds.member.models import Captcha, Profile

def image(request):
    """验证码图片"""
    
    captcha_text = Captcha(request).get()
    response = HttpResponse()
    if captcha_text:
        image = Image.new("RGBA", (captcha.LENGTH * captcha.FONT_SIZE - 26, captcha.FONT_SIZE), (0,0,0,0))
        canvas = ImageDraw.Draw(image)
        
        for i in range(0, len(captcha_text)):
            # font = ImageFont.truetype(choice(captcha.FONTS), captcha.FONT_SIZE)
            # canvas.text((captcha.FONT_SIZE*i+2, -4), captcha_text[i], font = font, fill = choice(captcha.COLOURS))
            horizon = 1; verticality  = -1
            if i>0: horizon = (captcha.FONT_SIZE - 5) * i
            if i%2 == 0: verticality = 2
            canvas.text((horizon, verticality), captcha_text[i], fill = choice(captcha.COLOURS))
            
        out = StringIO()
        image.save(out, "PNG")
        out.seek(0)
        response['Content-Type'] = 'image/png'
        response.write(out.read())
        
    return response

#===============================================================================
# 会员列表
#===============================================================================

@login_required
@cache_page(60 * 5)
def member_list(request, num_page = 1):
    '''会员列表'''
    
    num_page = int(num_page)
    context_dict = {
                    'user': request.user,
                    }
    #context_dict.update(_paginator_dict(user.objects.filter(is_active = True), num_page))
    
    t = loader.get_template('member/member_list.ouds')
    c = Context(context_dict,)
    
    return HttpResponse(t.render(c))

#========================================================
# 注册
#========================================================

from ouds.member.forms import RegistrationForm, SignInForm

def register(request, registration_form = RegistrationForm, template_name = 'member/registration_form.ouds'):
    """注册帐号"""

    if request.method == 'POST':
        data = request.POST
        data['captcha_text'] = Captcha(request).get()
        registration_form = registration_form(data, request.FILES, auto_id = False)
        if registration_form.is_valid():
            # 创建未激活用户
            profile = registration_form.save()
            # 上传图片
            if request.FILES:
                photo = request.FILES['photo']
                if photo.size < 30 * 1000:
                    profile.photo.save(str(profile.id) + photo.name[-4:], photo, save = True)
            
            return HttpResponseRedirect('/member/register/complete')
    else:
        registration_form = registration_form(auto_id = False)

    Captcha(request).create()

    return render_to_response(
            template_name,
            {'registration_form': registration_form,},
           )

#=================================================
# 帐号激活、登录、注销
#=================================================

from django.contrib.auth import authenticate, login, logout

def activate(request, vip_point, template_name = 'member/activate.ouds'):
    """帐号激活"""
    
    profile = Profile.objects.activate_user(vip_point.lower())
    try:
        user = profile.user
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponseRedirect('/city')
    except:
        return render_to_response(
                template_name,
                {'profile': profile,},
               )

#################################################

def sign_in(request, sign_in_form = SignInForm, template_name = 'member/sign_in.ouds'):
    """会员签入"""

    if request.method == "POST":
        data = request.POST.copy()
        data['captcha_text'] = Captcha(request).get()
        sign_in_form = sign_in_form(data, auto_id = False)
        if sign_in_form.is_valid():
            user = authenticate(username = data['username'].lower(), password = data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/city')
    else:
        sign_in_form = sign_in_form(auto_id = False)

    Captcha(request).create()

    return render_to_response(
            template_name,
            {'sign_in_form': sign_in_form,},
           )

####################################################

def sign_out(request, template_name = 'member/sign_out.ouds'):
    """全员签退"""

    logout(request)
    return render_to_response(
            template_name,
            {},
           )

######################################################

from ouds.member.models import TechElement

@login_required
def tech_list(request, template_name = 'member/tech_list.ouds'):
    """科技列表"""

    user = request.user
    profile = user.get_profile()
    city_id = request.session['city_id']

    tech_element_set = TechElement.objects.all()
    tech_element_list = []
    for tech_element in tech_element_set:
        tech_element_list.append(tech_element)
    tech_list = profile.tech_set.all()
    for tech in tech_list:
        for o in xrange(len(tech_element_list)):
            if tech_element_list[o] == tech.tech_element:
                del tech_element_list[o]
                break
    
    tech_researched_list = profile.tech_set.all()
    
    return render_to_response(
            template_name,
            {
                'user': user,
                'city': profile.city_set.get(id = city_id),
                'tech_element_list': tech_element_list,
                'tech_researched_list': tech_researched_list,
               },
           )

################################################

from ouds.utils.comms import _md5
from ouds.member.models import Tech, ImprovingTech

@login_required
def tech_research(request):
    """科技研发"""
    
    if request.method != 'POST':
        return HttpResponseRedirect('/city')

    user = request.user
    profile = user.get_profile()
    city_id = request.session['city_id']
    city = profile.city_set.get(id = city_id)

    # 研发科技
    tech_element = TechElement.objects.get(id = request.POST['tech_element_id'])
    
    # 当前时间
    now = datetime.datetime.now()
    
    # 研发科技
    tech = Tech()
    tech.id = _md5(request.user.username, now)
    tech.profile = profile
    tech.tech_element = tech_element
    tech.level = 0
    tech.save()
    
    # 加入升级序列
    improving_tech = ImprovingTech()
    improving_tech.id = _md5(request.user.username, now)
    improving_tech.profile = profile
    improving_tech.tech = tech
    improving_tech.level = 1
    latest_time = now
    if profile.improvingtech_set.count():
        latest_time = profile.improvingtech_set.latest('end_time').end_time
        if latest_time < now: latest_time = now
    improving_tech.end_time = latest_time + datetime.timedelta(seconds = tech_element.time)
    improving_tech.save()

    # 改变城市数值
    city.gold -= tech_element.gold
    city.save()

    return HttpResponse('reload')

################################################

from ouds.utils.templatetags.read import level_arithmetic

@login_required
def tech_improve(request):
    """科技提升"""
    
    if request.method != 'POST':
        return HttpResponseRedirect('/city')

    user = request.user
    profile = user.get_profile()
    city_id = request.session['city_id']
    city = profile.city_set.get(id = city_id)

    # 升级科技
    tech = Tech.objects.get(id = request.POST['tech_id'])
    level = tech.level + tech.improvingtech_set.count() + 1

    # 当前时间
    now = datetime.datetime.now()
    
    # 加入升级序列
    improving_tech = ImprovingTech()
    improving_tech.id = _md5(request.user.username, now)
    improving_tech.profile = profile
    improving_tech.tech = tech
    improving_tech.level = level
    latest_time = now
    if profile.improvingtech_set.count():
        latest_time = profile.improvingtech_set.latest('end_time').end_time
        if latest_time < now: latest_time = now
    improving_tech.end_time = latest_time + datetime.timedelta(seconds = level_arithmetic(level, tech.tech_element.time))
    improving_tech.save()

    # 改变城市数值
    city.gold -= level_arithmetic(level, tech.tech_element.gold)
    city.save()

    return HttpResponse('reload')

################################

from ouds.member.models import HelperCatalog

def helper_catalog(request, catalog_slug, template_name = 'member/helper_catalog.ouds'):
    """条目列表"""

    # 玩家默认语言
    language = request.META["HTTP_ACCEPT_LANGUAGE"].lower()
    if 'zh-cn' in language:
        language = 'zh-cn'
    elif 'zh-tw' in language:
        language = 'zh-tw'
    else:
        language = language[:2]
    
    helper_catalog = HelperCatalog.objects.get(slug = catalog_slug)

    return render_to_response(
            template_name,
            {
                'language': language,
                'helper_catalog': helper_catalog,
                },
           )

################################

def helper_entry(request, catalog_slug, language, entry_slug, template_name = 'member/helper_entry.ouds'):
    """帮助说明"""

    helper_catalog = HelperCatalog.objects.get(slug = catalog_slug)
    helper_entry = helper_catalog.helperentry_set.get(slug = entry_slug, is_public = True)

    return render_to_response(
            template_name,
            {
                'language': language,
                'helper_catalog': helper_catalog,
                'helper_entry': helper_entry,
                },
           )
