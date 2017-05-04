# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/auth/models.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: models file of auth module.
#===============================================================================

import datetime
import random

from django.conf import settings
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

###############################################

from ouds.member import captcha

class Captcha:
    '''验证码'''
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        
    @staticmethod
    def text():
        return ''.join([random.choice(captcha.LETTERS) for i in range(captcha.LENGTH)])
    
    def get(self):
        return self.request.session.get(captcha.NAME, '')
    
    def destroy(self):
        self.request.session[captcha.NAME] = ''
        
    def create(self):
        self.request.session[captcha.NAME] = self.text()


#######################################################

from ouds.utils.COMMON import MD5_RE, _md5

class ActivationManager(models.Manager):
    '''帐号激活管理器'''

    def activate_user(self, vip_point):
        if MD5_RE.search(vip_point):
            try:
                profile = self.get(vip_point = vip_point)
            except self.model.DoesNotExist:
                return _(u'此激活码不存在')
            
            if not profile.vip_point_expired():
                user = profile.user
                user.is_active = True
                user.save()

                profile.vip_end = datetime.datetime.now() + datetime.timedelta(days = 30)
                profile.vip_point = '60'
                profile.save()
                
                return profile
            
            return _(u'此激活码已过期')
        
        return _(u'此激活码无效')
    
    def create_inactive_user(self, username, type, email, password):
        
        # save new user
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()
        
        # save profile
        profile = self.create_profile(new_user, type)

        # 开城
        if profile:
            from ouds.city.models import City, BuildingElement, Building
            from ouds.map.models import Coordinate
            
            while True:
                from ouds.utils.CONSTANT import MIN_LONGITUDE, MAX_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE
                longitude = random.randint(MIN_LONGITUDE, MAX_LONGITUDE)
                latitude = random.randint(MIN_LATITUDE, MAX_LATITUDE)
                coordinate = Coordinate.objects.get(longitude = longitude, latitude = latitude)
                
                if coordinate.property not in (0, 1):
                    city = City.objects.filter(coordinate = coordinate)
                    if not city:
                        break
                    
            # 建都
            now = datetime.datetime.now()
            city = City.objects.create_city(now, _md5(username, now), profile, coordinate, \
                    profile.user.username + u'都城', is_capital = True, civilization_value = 12)
            # 初始化都城
            Building.objects.create(id = _md5('O' + username, now), city = city, building_element = BuildingElement(id = 39), \
                    location = 22, level = 1)
            Building.objects.create(id = _md5('U' + username, now), city = city, building_element = BuildingElement(id = 38), \
                    location = 20, level = 1)
            Building.objects.create(id = _md5('D' + username, now), city = city, building_element = BuildingElement(id = 37), \
                    location = 21, level = 1)
            Building.objects.create(id = _md5('S' + username, now), city = city, building_element = BuildingElement(id = 31), \
                    location = 14, level = 1)
            Building.objects.create(id = _md5('C' + username, now), city = city, building_element = BuildingElement(id = 30), \
                    location = 13, level = 1)
            Building.objects.create(id = _md5('G' + username, now), city = city, building_element = BuildingElement(id = 29), \
                    location = 12, level = 1)

        # send mail
        self.send_mail(username, email, profile.vip_point)

        return profile
    
    def create_profile(self, new_user, type):
        vip_point = _md5(new_user.username, datetime.datetime.now())
        return self.create(user = new_user, vip = 3, vip_end = datetime.datetime.now() + datetime.timedelta(days = 12), vip_point = vip_point, type = type)

    def send_mail(self, username, email, vip_point):
        from django.core.mail import send_mail

        expiration_days = settings.ACCOUNT_ACTIVATION_DAYS

        subject = ''.join(render_to_string('member/email_subject.ouds', {'username': username}).splitlines())
        message = render_to_string(
                'member/email_message.ouds',
                {
                    'username': username,
                    'vip_point': vip_point,
                    'expiration_days': expiration_days,
                   },
                )

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    def delete_expired_users(self):
        for profile in self.all():
            if profile.vip_point_expired():
                user = profile.user
                if not user.is_active:
                    user.delete()

#=========================================================
# extend user profile
#=========================================================

from ouds.utils.CONSTANT import VIP_TYPE, MEMBER_TYPE, SEX_TYPE, USER_AREA

class Profile(models.Model):
    '''国君详细资料'''
    
    user = models.OneToOneField(User, primary_key = True, verbose_name = _(u'国君帐号'))
    vip = models.PositiveSmallIntegerField(_(u'帐号类型'), choices = VIP_TYPE)
    vip_end = models.DateTimeField(_(u'贵宾期'), db_index = True)
    vip_point = models.CharField(_(u'贵宾点'), max_length = 32)
    is_public = models.BooleanField(_(u'信息公开'))
    type = models.PositiveSmallIntegerField(_(u'类型'), choices = MEMBER_TYPE, db_index = True)
    prestige = models.PositiveIntegerField(_(u'威望'), default = 0, db_index = True)
    union = models.PositiveIntegerField(_(u'盟邦'), null = True, blank = True, db_index = True)
    sex = models.CharField(_(u'性别'), max_length = 7, choices = SEX_TYPE)
    photo = models.ImageField(_(u'形象'), upload_to = 'imgs/member/profile', blank = True)
    birthday = models.DateField(_(u'生日'), blank = True, null = True, db_index = True)
    area = models.CharField(_(u'地域'), max_length = 2, choices = USER_AREA, db_index = True)
    phone = models.CharField(_(u'电话'), max_length = 30, blank = True)
    occupation = models.CharField(_(u'职业'), max_length = 50, blank = True)
    website = models.URLField(_(u'网址'), verify_exists = False, blank = True)
    description = models.TextField(_(u'描述'), blank = True)
    recommender = models.CharField(_(u'推荐人'), max_length = 30, blank = True, db_index = True)

    objects = ActivationManager()
    
    class Meta:
        verbose_name = _(u'国君资料')
        verbose_name_plural = _(u'国君资料')

    def __unicode__(self):
        return u'%s %s %s %s' % (self.user, MEMBER_TYPE[self.type][1], self.area, self.occupation)
    
    def vip_point_expired(self):
        expiration_date = datetime.timedelta(days = settings.ACCOUNT_ACTIVATION_DAYS)
        return self.user.date_joined + expiration_date <= datetime.datetime.now()

#=========================================================
# 盟邦信息
#=========================================================

class Union(models.Model):
    '''盟邦基本特征描述'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    name = models.CharField(_(u'盟邦名称'), unique = True, max_length = 6)
    photo = models.ImageField(_(u'盟邦形象'), upload_to = 'imgs/member/union', blank = True)
    website = models.URLField(_(u'盟邦总部'), verify_exists = False, blank = True)
    description = models.TextField(_(u'盟邦描述'))

    class Meta:
        verbose_name = _(u'盟邦信息')
        verbose_name_plural = _(u'盟邦信息')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.website,)

#=========================================================
# 消息报告
#=========================================================

from ouds.utils.CONSTANT import MESSAGE_FOLDER, MESSAGE_TYPE, MESSAGE_STATUS

class Message(models.Model):
    '''消息报告'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    profile = models.ForeignKey(Profile, verbose_name = _(u'归属人'), null = True, blank = True)
    title = models.CharField(_(u'标题'), max_length = 50)
    folder = models.PositiveSmallIntegerField(_(u'消息夹'), choices = MESSAGE_FOLDER)
    type = models.PositiveSmallIntegerField(_(u'类型'), choices = MESSAGE_TYPE)
    status = models.PositiveSmallIntegerField(_(u'状态'), choices = MESSAGE_STATUS)
    receiver = models.CharField(_(u'接收人'), max_length = 120)
    message = models.TextField(_(u'消息'))
    send_time = models.DateTimeField(_(u'发送时间'), editable = False)

    class Meta:
        verbose_name = _(u'消息报告')
        verbose_name_plural = _(u'消息报告')

    def __unicode__(self):
        return u'%s %s %s %s' % (self.profile, self.title, self.receiver, self.send_time)

#=========================================================
# 科技元素
#=========================================================

class TechElement(models.Model):
    '''科技元素'''
    
    name = models.CharField(_(u'名称'), unique = True, max_length = 50)
    code = models.CharField(_(u'编码'), unique = True, max_length = 50)
    civilization_value = models.PositiveSmallIntegerField(_(u'文明点数元量'))
    gold = models.PositiveSmallIntegerField(_(u'黄金消耗元量'))
    time = models.PositiveSmallIntegerField(_(u'时间元量/秒'))
    prestige = models.PositiveSmallIntegerField(_(u'威望点数'))
    tech_element = models.ManyToManyField('self', verbose_name = _(u'科技基础'), symmetrical = False, blank = True)

    class Meta:
        verbose_name = _(u'科技元素')
        verbose_name_plural = _(u'科技元素')
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.name, self.code, self.civilization_value, self.gold, self.time, self.prestige)

#=========================================================
# 国君科技
#=========================================================

class Tech(models.Model):
    '''科技信息'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    profile = models.ForeignKey(Profile, verbose_name = _(u'国君资料'))
    tech_element = models.ForeignKey(TechElement, verbose_name = _(u'科技元素'))
    level = models.PositiveSmallIntegerField(_(u'级别'))

    class Meta:
        verbose_name = _(u'科技信息')
        verbose_name_plural = _(u'科技信息')
        unique_together = ('profile', 'tech_element')
        ordering = ['profile']

    def __unicode__(self):
        return u'%s %s %s' % (self.profile, self.tech_element, self.level)

##########################################

class ImprovingTech(models.Model):
    '''国君正在升级的科技信息描述'''
    
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    profile = models.ForeignKey(Profile, verbose_name = _(u'国君资料'))
    tech = models.ForeignKey(Tech, verbose_name = _(u'科技信息'))
    level = models.PositiveSmallIntegerField(_(u'升级级别'))
    end_time = models.DateTimeField(_(u'完成时间'), db_index = True)

    class Meta:
        verbose_name = _(u'升级中科技')
        verbose_name_plural = _(u'升级中科技')
        unique_together = ('profile', 'tech', 'level')
        ordering = ['end_time']

    def __unicode__(self):
        return u'%s %s %s' % (self.tech, self.level, self.end_time)

####################

class HelperCatalog(models.Model):
    '''助手类别'''
    
    name = models.CharField(_(u'名称'), unique = True, max_length = 50)
    slug = models.SlugField(_(u'嵌条'), unique = True, max_length = 50)

    class Meta:
        verbose_name = _(u'助手类别')
        verbose_name_plural = _(u'助手类别')
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % (self.name,)

################################

from ouds.settings import LANGUAGES

class HelperEntry(models.Model):
    '''助手条目'''
    
    name = models.CharField(_(u'标题'), unique = True, max_length = 50)
    slug = models.SlugField(_(u'嵌条'), unique = True, max_length = 50)
    helper_catalog = models.ForeignKey(HelperCatalog, verbose_name=_(u'助手类别'))
    language = models.CharField(_(u'语言'), max_length = 5, choices = LANGUAGES)
    is_public = models.BooleanField(_(u'是否发布'))
    content = models.TextField(_(u'内容'),)
    last_date = models.DateTimeField(_(u'更新日期'))

    class Meta:
        verbose_name = _(u'助手条目')
        verbose_name_plural = _(u'助手条目')
        ordering = ['-last_date', 'name', 'helper_catalog']

    def __unicode__(self):
        return u'%s %s' % (self.name, self.helper_catalog.name)

#=========================================================
# 系统缺陷
#=========================================================

from ouds.utils.CONSTANT import BUG_LEVEL

class Bug(models.Model):
    '''系统缺陷'''
    
    title = models.CharField(_(u'标题'), max_length = 30)
    level = models.PositiveSmallIntegerField(_(u'级别'), choices = BUG_LEVEL)
    submitor = models.CharField(_(u'提交人'), max_length = 30, help_text = _(u'<font size="2" color="red">请测试一组人员正确填写，以便于联系、奖励。测试二组人员请勿更改</font>'))
    description = models.TextField(_(u'描述'))
    submit_time = models.DateTimeField(_(u'提交时间'), help_text = _(u'<font size="2" color="red">测试一组人员正确填写</font>'))
    is_bug = models.BooleanField(_(u'是否缺限'))
    is_corrected = models.BooleanField(_(u'是否更正'))
    correct_time = models.DateTimeField(_(u'更正时间'), blank = True, null = True, help_text = _(u'<font size="2" color="red">测试二组人员正确填写</font>'))
    reeditor = models.CharField(_(u'确认人'), max_length = 30, blank = True, null = True, help_text = _(u'<font size="2" color="red">测试一组人员不用填写。测试二组人员请正确填写，以便于联系、奖励</font>'))

    class Meta:
        verbose_name = _(u'系统缺陷')
        verbose_name_plural = _(u'系统缺陷')
        ordering = ['-submit_time', 'level']
        unique_together = ('title', 'submitor')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.title, BUG_LEVEL[self.level][1], self.submitor, self.submit_time, self.is_corrected, self.reeditor)

