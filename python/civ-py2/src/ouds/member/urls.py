# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/auth/urls.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: urls file of auth module.
#===============================================================================

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('ouds.member.views',
        (r'^captcha.png$', 'image'),

        (r'^(\d+)/$', 'member_list'),
        url(r'^register/$', 'register', name='register'),
        url(r'^register/complete/$', direct_to_template, {'template': 'member/registration_complete.ouds'}, name = 'register_complete'),
        url(r'^activate/(\w+)/$', 'activate', name='activate'),
        url(r'^sign_in/$', 'sign_in', name='sign_in'),
        url(r'^sign_out/$', 'sign_out', name='sign_out'),
        url(r'^profile/$', direct_to_template, {'template': 'member/profile.ouds'}, name = 'profile'),
        url(r'^password/change/$', auth_views.password_change, name='password_change'),
        url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
        url(r'^password/reset/$', auth_views.password_reset, name='password_reset'),
        url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),

        (r'^tech/list/$', 'tech_list'),
        (r'^tech/research/$', 'tech_research'),
        (r'^tech/improve/$', 'tech_improve'),

        url(r'^vip/$', direct_to_template, {'template': 'member/vip.ouds'}, name = 'vip'),
        url(r'^warning/$', direct_to_template, {'template': 'member/warning.ouds'}, name = 'warning'),
        url(r'^helper/$', direct_to_template, {'template': 'member/helper.ouds'}, name = 'helper'),
        (r'^helper/([^/]+)/$', 'helper_catalog'),
        (r'^helper/([^/]+)/([^/]+)/([^/]+)/$', 'helper_entry'),
       )
