# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: postmaster@gaiding.com
# File Name: ouds/settings.py
# Revision: 0.1
# Date: 2007-2-5 17:48
# Description: settings.
#===============================================================================

DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
        (u'长弓骛之', 'ourunix@gmail.com'),
       )

MANAGERS = ADMINS

DATABASE_ENGINE       = 'postgresql_psycopg2'
DATABASE_NAME         = 'oudsus_civ'
#DATABASE_SCHEMA      = 'test'
DATABASE_USER         = 'oudsus'
DATABASE_PASSWORD     = 'Ouds~us3.141'
DATABASE_HOST         = ''
DATABASE_PORT         = ''

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

USE_I18N = True

LOCALE_PATHS = (
        '/home/oudsus/Ouds/civ/locale',
       )

LANGUAGES = (
        ('zh-cn', u'简体中文'),
        ('zh-tw', u'繁體中文'),
        ('en', u'English'),
        ('de', u'Deutsch'),
        ('fr', u'Français'),
        ('it', u'Italiano'),
        ('pt', u'Português'),
        ('es', u'Español'),
        ('sv', u'Svenska'),
        ('ru', u'Русский'),
        ('jp', u'日本語'),
        ('ko', u'한국어'),
       )

SITE_ID = 1

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '1m&um8ppxd-_!%!$i07r8v3+ij32jn^#%_61w$9zg5hnoy#8&z'

TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.load_template_source',
        'django.template.loaders.app_directories.load_template_source',
       )

MIDDLEWARE_CLASSES = (
#        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.doc.XViewMiddleware',
#        'django.middleware.cache.FetchFromCacheMiddleware',
       )

ROOT_URLCONF = 'ouds.urls'

TEMPLATE_DIRS = (
        '/home/oudsus/Ouds/civ/templates',
       )

MEDIA_ROOT = '/home/oudsus/Ouds/civ/media'

MEDIA_URL = '/media/'

INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',
        
        'ouds.utils',
        'ouds.member',
        'ouds.map',
        'ouds.city',
        'ouds.trade',
       )

#===============================================================================
# extend settings
#===============================================================================

TEMPLATE_STRING_IF_INVALID = 'Ouds'

AUTH_PROFILE_MODULE = 'member.profile'
LOGIN_URL = '/member/sign_in'

FILE_UPLOAD_MAX_MEMORY_SIZE = 30 * 1000

#===============================================================================
# define for active memeber
#===============================================================================

EMAIL_HOST = 'mail.ouds.us'
EMAIL_PORT = '26'
EMAIL_HOST_USER = 'admin@ouds.us'
EMAIL_HOST_PASSWORD = 'wenming'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@ouds.us'
ACCOUNT_ACTIVATION_DAYS = 7

# session and cache
SESSION_COOKIE_AGE = 60 * 60 # 1 hour

#CACHE_BACKEND = 'locmem:///'
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_SECONDS = 60 * 5 # 5 minutes
#CACHE_MIDDLEWARE_KEY_PREFIX = 'ouds'

