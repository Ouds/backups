# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: ouds/settings.py
# Revision: 0.1
# Date: 2007-2-5 17:48
# Description: settings.
#===============================================================================

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
        (u'长弓骛之', 'ourunix@gmail.com'),
       )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2',
        'NAME': 'ls',
        'USER': 'oudsus',
        'PASSWORD': 'oudsus',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

LOCALE_PATHS = (
    '../locale',
)

LANGUAGES = (
    ('zh-cn', u'简体中文'),
    ('zh-tw', u'繁體中文'),
    ('en', u'English'),
    ('de', u'Deutsch'),
#    ('fr', u'Français'),
#    ('it', u'Italiano'),
#    ('pt', u'Português'),
#    ('es', u'Español'),
#    ('sv', u'Svenska'),
#    ('ru', u'Русский'),
#    ('jp', u'日本語'),
#    ('ko', u'한국어'),
)

MEDIA_ROOT = '../medias'

MEDIA_URL = '/medias/'

ADMIN_MEDIA_PREFIX = '/medias/admin/'

SECRET_KEY = '_0+muz@!_g_r1suj-tiyw=k8u0q%n_(ie_ob0b8o%2_@a_!%&0'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'ouds.urls'

TEMPLATE_DIRS = (
    '../templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',

    'ouds.utils',
    'ouds.member',
    'ouds.article',
)

#===============================================================================
# extend settings
#===============================================================================

TEMPLATE_STRING_IF_INVALID = 'LoSpring.com'
HOST_URL = 'http://LoSpring.com'

AUTH_PROFILE_MODULE = 'member.profile'
LOGIN_URL = '/member/sign_in'

FILE_UPLOAD_MAX_MEMORY_SIZE = 300 * 1000

ICON_SIZE = 20 * 1000
IMAGE_SIZE = 300 * 1000

#===============================================================================
# define for active memeber
#===============================================================================

EMAIL_HOST = 'mail.dingdongquan.com'
EMAIL_PORT = '26'
EMAIL_HOST_USER = 'webmaster@dingdongquan.com'
EMAIL_HOST_PASSWORD = 'hgkupqtd'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'webmaster@dingdongquan.com'
ACCOUNT_ACTIVATION_DAYS = 7

# session and cache
SESSION_COOKIE_AGE = 60 * 60 # 1 hour

#CACHE_BACKEND = 'locmem:///'
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_SECONDS = 60 * 5 # 5 minutes
#CACHE_MIDDLEWARE_KEY_PREFIX = 'ouds'

